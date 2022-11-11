/**
 * @param {number[][]} bookings
 * @param {number} n
 * @return {number[]}
 */
var corpFlightBookings = function (bookings, n) {
   let res = new Array(n+1).fill(0)

   for(let book of bookings){
       res[book[0]-1]+=book[2]
       res[book[1]]-=book[2]
   }

// caculating prefix sum
   sum=0
   for(let index=0;index<=n;index++){
       sum+=res[index]
       res[index]=sum
   }
    res=res.slice(0,n)
   return res
};
