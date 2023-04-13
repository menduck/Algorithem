/*
# 문제 접근
- record를 순회하면서 상태(입장/퇴장)를 확인한다.
- map을 사용해 id => nickname 쌍을 업데이트 한다.
  - 퇴장(Leave)할땐 제외한다.(nickname변화 없으므로)
- 그 다음 record 반복을 다시 돌면서 map객체의 id 값(nickname)과 문자열을 result에 추가한다.
*/

function solution(record) {
  const recordMap = new Map();
  const result = [];
    for (ele of record){
      let [state, id, nickname] = ele.split(' ');
      if (state !== 'Leave'){
        recordMap.set(id,nickname)
      } 
    }
    // console.log(recordMap) Map(2) { 'uid1234' => 'Prodo', 'uid4567' => 'Ryan' }

    for(let i=0;i<record.length;i++){
      const [state, id, nickname] = record[i].split(' ')
      if (state === 'Enter'){
        result.push(`${recordMap.get(id)}님이 들어왔습니다.`)
      } else if((state === 'Leave')){
        result.push(`${recordMap.get(id)}님이 나갔습니다.`)
      }
    }
    return result
}

// 다른 사람 코드

function solution(record) {
  let answer = [];
  const map = new Map();
  
  for (let i = 0; i < record.length; ++i) {
      const [state, uid, name] = record[i].split(' ');
      
      if (state == 'Leave') {
          answer.push([uid, '님이 나갔습니다.']);
          
          continue;
      }
      
      if (state == 'Enter') {
          answer.push([uid, '님이 들어왔습니다.']);
      }

      map.set(uid, name);
  }
  
  return answer.map(ele => map.get(ele[0]) + ele[1]);
}

console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", 'Leave uid4567']))
// console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

/*
# 배운점
## Map
### Object vs Map
- Object
  - key : 문자열 또는 심벌 값, 중복된 값 X
  - 이터러블 하지 않음.
  - 요소 개수 확인 시 Object.key(obj).length
- Map
  - key : 객체를 포함한 모든 값, 중복된 값 X
  - 이터러블 함
  - 요소 개수 확인 시 map.size


*/