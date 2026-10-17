
const { DateTime } = luxon;

const CHINA_ZONE = "Asia/Shanghai";
const SWEDEN_ZONE = "Europe/Stockholm";
const MINUTES_PER_DAY = 1440;

function toMinutes(timeString) {
    const [hours, minutes] = timeString.split(":").map(Number);
    return hours * 60 + minutes;
}

function toTime(totalMinutes) {
    totalMinutes =
        ((totalMinutes % MINUTES_PER_DAY) + MINUTES_PER_DAY)
        % MINUTES_PER_DAY;

    const hours = Math.floor(totalMinutes / 60);
    const minutes = totalMinutes % 60;

    return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}`;
}

function displayTime(totalMinutes) {
    if (totalMinutes === MINUTES_PER_DAY) {
        return "24:00";
    }

    return toTime(totalMinutes);
}

// Calculate free periods using one person's local clock.

function getFreePeriods(
    sleepStart,
    sleepDuration,
    preparation,
    morningRoutine
) {
    const sleepStartMin = toMinutes(sleepStart);

    const wakeUpMin =
        (sleepStartMin + sleepDuration * 60) % MINUTES_PER_DAY;

    const freeStart =
        (wakeUpMin + morningRoutine * 60) % MINUTES_PER_DAY;

    const freeEnd =
        ((sleepStartMin - preparation * 60) % MINUTES_PER_DAY
            + MINUTES_PER_DAY) % MINUTES_PER_DAY;

    if (freeStart === freeEnd) {
        return { wakeUp: toTime(wakeUpMin), periods: [] };
    }

    if (freeStart < freeEnd) {
        return {
            wakeUp: toTime(wakeUpMin),
            periods: [{
                start: freeStart,
                end: freeEnd,
                dayOffset: 0
            }]
        };
    }

    return {
        wakeUp: toTime(wakeUpMin),
        periods: [
            {
                start: freeStart,
                end: MINUTES_PER_DAY,
                dayOffset: 0
            },
            {
                start: 0,
                end: freeEnd,
                dayOffset: 1
            }
        ]
    };
}


// Convert a local date and minute-of-day into a real instant.
// Luxon applies the correct time-zone rules for that date.
function localTimeToMillis(dateString, minutes, zone) {
    let date = DateTime.fromISO(dateString, { zone });

    if (!date.isValid) {
        throw new Error(`Invalid date: ${dateString}`);
    }

    if (minutes === MINUTES_PER_DAY) {
        date = date.plus({ days: 1 }).startOf("day");
    } else {
        date = date.startOf("day").plus({ minutes });
    }

    if (!date.isValid) {
        throw new Error("Could not convert the selected local time.");
    }

    return date.toMillis();
}

// Turn local-clock free periods into absolute time intervals.
function toAbsolutePeriods(periods, dateString, zone) {
    return periods.map(period => {
        const localDate = DateTime
            .fromISO(dateString, { zone })
            .plus({ days: period.dayOffset })
            .toISODate();

        return {
            start: localTimeToMillis(
                localDate, period.start, zone
            ),
            end: localTimeToMillis(
                localDate, period.end, zone
            )
        };
    });
}

// Include free periods from nearby local dates,
// so periods crossing midnight are not missed.
function getAbsolutePeriodsAroundDate(periods, dateString, zone) {
    const allPeriods = [];

    for (let offset = -2; offset <= 2; offset++) {
        const baseDate = DateTime
            .fromISO(dateString, { zone })
            .plus({ days: offset })
            .toISODate();

        allPeriods.push(
            ...toAbsolutePeriods(periods, baseDate, zone)
        );
    }

    return allPeriods;
}

// Find overlapping intervals on the absolute timeline.
function findOverlaps(firstPeriods, secondPeriods) {
    const overlaps = [];

    for (const first of firstPeriods) {
        for (const second of secondPeriods) {
            const start = Math.max(first.start, second.start);
            const end = Math.min(first.end, second.end);

            if (start < end) {
                overlaps.push({ start, end });
            }
        }
    }

    overlaps.sort((a, b) => a.start - b.start);

    // Merge intervals that touch or overlap.
    const merged = [];

    for (const period of overlaps) {
        const last = merged[merged.length - 1];

        if (last && period.start <= last.end) {
            last.end = Math.max(last.end, period.end);
        } else {
            merged.push({ ...period });
        }
    }

    return merged;
}

function formatInZone(timestamp, zone) {
    return DateTime.fromMillis(timestamp, { zone }).toFormat("HH:mm");
}

function formatPeriods(periods, zone) {
    if (periods.length === 0) {
        return "<p>No free time found.</p>";
    }

    return periods.map(period => `
        <p>
            ${formatInZone(period.start, zone)}
            – ${formatInZone(period.end, zone)}
        </p>
    `).join("");
}

const form = document.getElementById("schedule-form");
const results = document.getElementById("results");
const dateInput = document.getElementById("meeting-date");

const copyButton = document.getElementById("copy-results-button");
const copyStatus = document.getElementById("copy-status");

let shareMessage = "";

// Default to tomorrow on the user's local calendar.
const tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);

const year = tomorrow.getFullYear();
const month = String(tomorrow.getMonth() + 1).padStart(2, "0");
const day = String(tomorrow.getDate()).padStart(2, "0");
const tomorrowString = `${year}-${month}-${day}`;

dateInput.min = tomorrowString;
dateInput.value = tomorrowString;

form.addEventListener("submit", function (event) {
    event.preventDefault();

    if (!luxon || !DateTime) {
        results.textContent =
            "The date-time library did not load. Please check your internet connection and refresh.";
        return;
    }

    const selectedDate = dateInput.value;

    if (!selectedDate) {
        results.textContent = "Please choose a date.";
        return;
    }

    try {
        // Read Mika's settings.
        const mikaSleepStart =
            document.getElementById("mika-sleep-start").value;
        const mikaSleepDuration =
            Number(document.getElementById("mika-sleep-duration").value);
        const mikaPreparation =
            Number(document.getElementById("mika-before-sleep").value);
        const mikaMorningRoutine =
            Number(document.getElementById("mika-after-waking").value);

        // Read Shuyu's settings.
        const shuyuSleepStart =
            document.getElementById("shuyu-sleep-start").value;
        const shuyuSleepDuration =
            Number(document.getElementById("shuyu-sleep-duration").value);
        const shuyuPreparation =
            Number(document.getElementById("shuyu-before-sleep").value);
        const shuyuMorningRoutine =
            Number(document.getElementById("shuyu-after-waking").value);

        // Calculate each person's local free periods.
        const mika = getFreePeriods(
            mikaSleepStart,
            mikaSleepDuration,
            mikaPreparation,
            mikaMorningRoutine
        );

        const shuyu = getFreePeriods(
            shuyuSleepStart,
            shuyuSleepDuration,
            shuyuPreparation,
            shuyuMorningRoutine
        );

        // Convert both schedules to the same absolute timeline.
        const mikaAbsolute = toAbsolutePeriods(
            mika.periods, selectedDate, SWEDEN_ZONE
        );

        const shuyuAbsolute = toAbsolutePeriods(
            shuyu.periods, selectedDate, CHINA_ZONE
        );

        // Find the periods when both people are free.
//        const sharedPeriods = findOverlaps(
//            mikaAbsolute, shuyuAbsolute
//        );
          // Calculate schedules across nearby dates.
          const mikaPeriodsAroundDate = getAbsolutePeriodsAroundDate(
              mika.periods, selectedDate, SWEDEN_ZONE
          );

          const shuyuPeriodsAroundDate = getAbsolutePeriodsAroundDate(
              shuyu.periods, selectedDate, CHINA_ZONE
          );

          // Find all overlapping periods.
          const allSharedPeriods = findOverlaps(
              mikaPeriodsAroundDate,
              shuyuPeriodsAroundDate
          );

          // Keep only shared time within the selected China calendar day.
          const chinaDayStart = DateTime
              .fromISO(selectedDate, { zone: CHINA_ZONE })
              .startOf("day")
              .toMillis();

          const chinaDayEnd = DateTime
              .fromISO(selectedDate, { zone: CHINA_ZONE })
              .plus({ days: 1 })
              .startOf("day")
              .toMillis();

          const sharedPeriods = allSharedPeriods
              .map(period => ({
                  start: Math.max(period.start, chinaDayStart),
                  end: Math.min(period.end, chinaDayEnd)
              }))
              .filter(period => period.start < period.end);


//        const messageLines = [
//            `Shared free time for ${selectedDate}`,
//            ""
//        ];
        const messageLines = [`🐝 Shared free time for ${selectedDate}`, ""];

        if (sharedPeriods.length === 0) {
            messageLines.push("No overlapping free time found.");
        } else {
            for (const period of sharedPeriods) {
                const chinaStart = DateTime.fromMillis(period.start, {
                    zone: CHINA_ZONE
                }).toFormat("yyyy-MM-dd HH:mm");

                const chinaEnd = DateTime.fromMillis(period.end, {
                    zone: CHINA_ZONE
                }).toFormat("yyyy-MM-dd HH:mm");

                const swedenStart = DateTime.fromMillis(period.start, {
                    zone: SWEDEN_ZONE
                }).toFormat("yyyy-MM-dd HH:mm");

                const swedenEnd = DateTime.fromMillis(period.end, {
                    zone: SWEDEN_ZONE
                }).toFormat("yyyy-MM-dd HH:mm");

                messageLines.push(
                    `China: ${chinaStart} – ${chinaEnd}`,
                    `Sweden: ${swedenStart} – ${swedenEnd}`,
                    ""
                );
            }
        }

        shareMessage = messageLines.join("\n").trim();
        copyButton.disabled = sharedPeriods.length === 0;
        copyStatus.textContent = "";


        // Display the selected date and both local time zones.
        const chinaDate = DateTime.fromISO(selectedDate, {
            zone: CHINA_ZONE
        }).toFormat("MMMM d, yyyy");

        const swedenDate = DateTime.fromISO(selectedDate, {
            zone: SWEDEN_ZONE
        }).toFormat("MMMM d, yyyy");

        results.innerHTML = `
            <h3>Selected Date</h3>
            <p>China: ${chinaDate}</p>
            <p>Sweden: ${swedenDate}</p>

            <h3>Mika's Schedule 🇸🇪</h3>
            <p>Wake-up time: ${mika.wakeUp}</p>
            <p>Free time (Sweden time):</p>
            ${formatPeriods(mikaAbsolute, SWEDEN_ZONE)}

            <h3>Shuyu's Schedule 🇨🇳</h3>
            <p>Wake-up time: ${shuyu.wakeUp}</p>
            <p>Free time (China time):</p>
            ${formatPeriods(shuyuAbsolute, CHINA_ZONE)}

            <h3>Shared Free Time 🐝</h3>
            ${
                sharedPeriods.length === 0
                    ? "<p>No overlapping free time on this date. Try another date or adjust the schedules.</p>"
                    : sharedPeriods.map(period => `
                        <p>
                            <strong>China:</strong>
                            ${formatInZone(period.start, CHINA_ZONE)}
                            – ${formatInZone(period.end, CHINA_ZONE)}
                        </p>
                        <p>
                            <strong>Sweden:</strong>
                            ${formatInZone(period.start, SWEDEN_ZONE)}
                            – ${formatInZone(period.end, SWEDEN_ZONE)}
                        </p>
                        <hr>
                    `).join("")
            }
        `;
    } catch (error) {
        console.error(error);
        results.textContent =
            "Something went wrong while calculating the schedules. Please check your inputs and try again.";
    }
});


copyButton.addEventListener("click", async function () {
    if (!shareMessage) {
        copyStatus.textContent = "Please calculate the shared free time first.";
        return;
    }

    try {
        await navigator.clipboard.writeText(shareMessage);
//        copyStatus.textContent = "Copied! You can now send it to Shuyu.";
        copyStatus.textContent = "Copied! You can now paste it anywhere.";
    } catch (error) {
        copyStatus.textContent =
            "Copy failed. Please open the page in a secure context and try again.";
        console.error(error);
    }
});
