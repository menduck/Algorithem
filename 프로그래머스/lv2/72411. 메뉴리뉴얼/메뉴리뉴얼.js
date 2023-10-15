/**
 * 접근 방법
 * - 조합 함수로 course별 조합을 구한다.
 * - 유니크한 조합을 추려낸 다음, 조합 하나씩 비교해서 count한다. => 객체
 * - count가 2 이상인 조합들을 추려내고 알파벳 순서대로 arr에 담아 반환한다.
 */

function solution(orders, course) {
  let resultObj = {};
  let uniqueCobi = [];

  orders.forEach((order, i) => {
    course.forEach((num) => {
      const orderArr = order.split('');
      const combinations = getCombinations(orderArr, num);
      combinations.forEach((combination) => {
        const str = combination.sort().join('');
        if (!uniqueCobi.includes(str)) {
          return uniqueCobi.push(str);
        }
      });
    });
  });

  uniqueCobi.forEach((singleMenu) => {
      if (!resultObj[singleMenu]) {
        resultObj[singleMenu] = 0;
      }
      // singleMenu = 'AB'
      for (let j = 0; j < orders.length; j++) {
        const restOrder = orders[j]; // 'AABC'

        const pattern = singleMenu.split('').join('|'); // A|B
        const regex = new RegExp(pattern, 'g'); 
        const singleMenuCount =
          (restOrder.match(regex) || []).length === singleMenu.length ? 1 : 0;
        resultObj[singleMenu] += singleMenuCount;
      }
    });

    const arr = Object.entries(resultObj)
    const result = []
    for(let i = 0 ; i < course.length; i++){
      const sameLen = arr.filter(v => v[0].length === course[i])
      const sameLenValue = sameLen.map(v => v[1])
      const max = Math.max(...sameLenValue)
      if(max === 1){
        break
      }
      const maxMenu = sameLen.filter(v => v[1] === max)
      result.push(...maxMenu)

    }

    const sortedData =result.sort((a, b) => {
      let menuA = a[0]
      let menuB = b[0]

      if(menuA > menuB) return 1
      if(menuA < menuB) return -1
      
    })

  return sortedData.map(v => v[0]);
}

/** 조합 */
function getCombinations(arr, num) {
  const result = [];
  if (num === 1) return arr;
  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combinations = getCombinations(rest, num - 1);
    const attached = combinations.map((v) => [fixed, ...v]);
    result.push(...attached);
  });

  return result;
}

solution(["XYZ"], [2, 3, 4]);
// solution(["XYZ", "XWY", "WXA"], [2, 3, 4]);
// solution(['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH'], [2, 3, 4]);

// 다른 사람 풀이
function solution(orders, course) {
  const ordered = {};
  const candidates = {};
  const maxNum = Array(10 + 1).fill(0);
  const createSet = (arr, start, len, foods) => {
    if (len === 0) {
      ordered[foods] = (ordered[foods] || 0) + 1;
      if (ordered[foods] > 1) candidates[foods] = ordered[foods];
      maxNum[foods.length] = Math.max(maxNum[foods.length], ordered[foods]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      createSet(arr, i + 1, len - 1, foods + arr[i]);
    }
  };

  orders.forEach((od) => {
    // arr.sort는 기본적으로 사전식 배열
    const sorted = od.split('').sort();
    // 주문한 음식을 사전순으로 배열해서 문자열을 만든다.
    // course에 있는 길이만 만들면 된다.
    course.forEach((len) => {
      createSet(sorted, 0, len, '');
    });
  });

  const launched = Object.keys(candidates).filter(
    (food) => maxNum[food.length] === candidates[food]
  );

  return launched.sort();
}