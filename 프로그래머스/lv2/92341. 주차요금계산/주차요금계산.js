function solution(fees, records) {
  const recordsArray = records.map((v) => v.split(" "));

  let usageTimes = {};
  let isParkingObj = {};

  for (let i = 0; i < records.length; i++) {
    const car = parseInt(recordsArray[i][1]);
    const time = recordsArray[i][0];
    const inOrOut = recordsArray[i][2];

    const usageTime = getMinut(time);
    // 새로 작성
    if(inOrOut === "IN"){
      usageTimes[car] = (usageTimes[car] ?? 0) -usageTime
      // usageTimes[car] = (usageTimes[car] || 0) -usageTime
      isParkingObj[car] = true
    } else {
      usageTimes[car] += usageTime;
      isParkingObj[car] = false;

    }
    // if (usageTimes[car] || usageTimes[car] === 0) {
    //   // 빈 객체가 아니고
    //   if (inOrOut === "IN") {
    //     //  -사용시간 누적
    //     usageTimes[car] -= usageTime;
    //     isParkingObj[car] = true;
    //   } else {
    //     // 빈 객체가 아니고 OUT
    //     usageTimes[car] += usageTime;
    //     isParkingObj[car] = false;
    //   }
    // } else {
    //   // 빈 객체
    //   if (inOrOut === "IN") {
    //     //  -사용시간 누적
    //     usageTimes[car] = -usageTime;
    //     isParkingObj[car] = true;
    //   }
    // }
  }
  const parkingCars = Object.keys(usageTimes).filter(
    (car) => isParkingObj[car]
  );
  parkingCars.forEach((parkingCar) => (usageTimes[parkingCar] += 23 * 60 + 59));

  // 차량번호 오름차순 정렬
  Object.keys(usageTimes).sort((a, b) => a - b);

  console.log(usageTimes) 

  return Object.entries(usageTimes).map((v) => {
      if (v[1] > fees[0]) {
        return fees[1] + Math.ceil((v[1] - fees[0]) / fees[2]) * fees[3];
      } else {
        return fees[1];
      }
    });
}

function getMinut(time) {
  // '5:34'
  const timeArray = time.split(":").map((v) => parseInt(v)); // [5,34]

  return timeArray[0] * 60 + timeArray[1]; // 5*60+34 = 334
}


solution(
  [180, 5000, 10, 600],
  [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
  ]
);


// 삽질
```
solution([1, 10, 1, 11], ["00:00 1234 IN", "00:02 1234 OUT"])일때,
usageTimes[car] = 0 임으로 첫번째 조건문에서 빈 객체라고 판단하

```