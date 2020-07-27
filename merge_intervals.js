var merge = function(intervals) {
    if (intervals.length <= 1) {
        return intervals;
    }

    intervals.sort((a,b) => a[0] - b[0]);

    for (let i = 0; i <= intervals.length; i++) {
        for (let j = i + 1; j <= intervals.length; j++) {
            const current = intervals[i];
            const next = intervals[j];


            if (current && next && current[1] >= next[0]) {
                current[0] = Math.min(current[0], next[0])
                current[1] = Math.max(current[1], next[1])
                intervals.splice(j, 1)
                j -=1

            }
        }
    }

    return intervals;
};

const merge = function(intervals) {
    if (intervals.length <= 1) {
        return intervals;
    }

    intervals.sort((a,b) => a[0] - b[0]);

    for (let i = 0; i <= intervals.length; i++) {
        const current = intervals[i];
        const next = intervals[i + 1];


        if (current && next && current[1] >= next[0]) {
            current[0] = Math.min(current[0], next[0])
            current[1] = Math.max(current[1], next[1])
            intervals.splice(i+1, 1)
            i -=1

        }
    }

    return intervals;
};