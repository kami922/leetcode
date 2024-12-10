/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    const n = gas.length;
      let totalSurplus = 0, surplus = 0, start = 0;

      for (let i = 0; i < n; i++) {
        totalSurplus += gas[i] - cost[i];
        surplus += gas[i] - cost[i];

        if (surplus < 0) {
          surplus = 0;
          start = i + 1;
        }
      }

      return totalSurplus < 0 ? -1 : start;
    
};