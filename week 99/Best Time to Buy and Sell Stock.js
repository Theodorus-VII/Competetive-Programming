/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let i = 0;
    let j = 1;
    let profit = 0;
    
    while (j < prices.length){
        if (prices[j]<prices[i]){
            i = j;    
        }
        else if (prices[j] > prices[i]){
            if (prices[j] - prices[i] > profit){
                profit = prices[j] - prices[i];
            }
        }
        j ++;
    }
    console.log(profit);
    return profit;
};
maxProfit([1,2,3,4])