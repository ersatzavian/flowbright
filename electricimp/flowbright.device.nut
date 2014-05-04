
const ML_PER_PULSE = 2.0;
const READTIME = 0.099;
const YIELDTIME = 0.001;
const UPDATE_AGENT_INTERVAL = 10; // seconds

pulses_this_min <- 0;
reads_this_min <- 0;
reads_per_update <- UPDATE_AGENT_INTERVAL / (READTIME + YIELDTIME);

function nearestminute() {
    local now = time();
    local seconds = now % 60;
    if (seconds < 30) { now -= seconds; }
    else { now += (60 - seconds) }
    return now;
}

function count() {
    imp.wakeup(YIELDTIME+READTIME, count);
    pulses_this_min += pulsepin.read();
    if (reads_this_min++ >= reads_per_update) {
        agent.send("update", {"id":hardware.getdeviceid(),"time":nearestminute(),"volume":(pulses_this_min * ML_PER_PULSE)});
        reads_this_min = 0;
        pulses_this_min = 0;
    }
}

pulsepin <- hardware.pin1;
pulsepin.configure(PULSE_COUNTER, READTIME);

agent.send("update", {"id":hardware.getdeviceid(),"time":nearestminute(),"volume":(pulses_this_min * ML_PER_PULSE)});

count();