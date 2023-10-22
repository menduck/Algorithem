function solution(m, musicinfos) {
  const result = {};
  const newM = m.replace(/(C|D|F|G|A)#/g, (_, p1) => p1.toLowerCase());
  for (let unit of musicinfos) {
    let [startTime, endTime, title, musicCode] = unit.split(',');
    let [startHour, startMin] = startTime
      .split(':')
      .map((v) => parseInt(v, 10));
    let [endHour, endMin] = endTime.split(':').map((v) => parseInt(v, 10));
    // 노래 재생 시간
    const playingTime = (endHour - startHour) * 60 + (endMin - startMin);
    const newMusicCode = musicCode.replace(/(C|D|F|G|A)#/g, (_, p1) =>
      p1.toLowerCase()
    );
    const musicTime = newMusicCode.length;
    const repeatNum = Math.ceil(playingTime / musicTime);
    const playingCode = newMusicCode.repeat(repeatNum).slice(0, playingTime);

    const playingCodeArr = playingCode.split(newM);
    if (playingCodeArr.length !== 1) {
      result[title] = playingTime;
    }
  }

  const resultArr = Object.entries(result);
  if (resultArr.length > 0) {
    // 재생시간 긴 순서로 정렬
    answer = resultArr.sort((a, b) => b[1] - a[1])[0][0];
  } else {
    answer = '(None)';
  }

  console.log(answer);
  return answer;
}
// solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']);
// solution('CC#BCC#BCC#BCC#B', [
//   '03:00,03:30,FOO,CC#B',
//   '04:00,04:08,BAR,CC#BCC#BCC#B',
// ]);
// solution('A', ['12:00,12:01,Song,A']);
// solution('A', ['12:00,12:01,Song,BA']); // "(None)"
// solution('BA', ['12:00,12:04,Song,A#B']); // "(None)"
solution('BA', ['12:00,12:02,Song,AB']); // "(None)"
solution('BA', ['12:00,12:03,Song,AB']); // "Song"
solution('A', ['12:00,12:01,Song,A#']); // "(None)"
solution('A#', ['12:00,12:01,Song,A#']); //  "Song"
solution('ABA', ['12:00,13:00,Song,AB']); //  "Song"
solution('A', ['12:00,12:01,Sing,A', '12:00,12:01,Song,A']); //sing
solution('A', ['12:00,12:01,Sing,A', '12:00,13:00,Song,A']); //"Song"
// 실패 2 - 문자열로 처리하면 '#'의 대한 처리를 계속 해줘야 함.
// function solution(m, musicinfos) {
//   const result = {};
//   let answer = '';
//   for (let unit of musicinfos) {
//     let [startTime, endTime, title, musicCode] = unit.split(',');
//     let [startHour, startMin] = startTime
//       .split(':')
//       .map((v) => parseInt(v, 10));
//     let [endHour, endMin] = endTime.split(':').map((v) => parseInt(v, 10));
//     let playingTime = (endHour - startHour) * 60 + (endMin - startMin);
//     let musicTime = musicCode.length;
//     let sharpCount = musicCode.split('#').length - 1;
//     let totalCodeCount = playingTime + sharpCount;
//     let repeatNum = Math.ceil(totalCodeCount / musicTime);

//     let playingCode = musicCode.repeat(repeatNum).slice(0, totalCodeCount + 1);
//     if (playingCode.slice(-1) !== '#' && playingCode.length !== 1) {
//       playingCode = playingCode.slice(0, -1);
//     }
//     const playingCodeArr = playingCode.split(m); // ABC ABC#DF '' #DF
//     if (playingCodeArr.length !== 1) {
//       if (playingCode[1] && playingCode[1].slice(0) !== '#') {
//         result[title] = playingTime;
//       }
//       if(playingCodeArr.every((el) => !el)){
//         result[title] = playingTime;
//       }
//     }
//   }

//   const resultArr = Object.entries(result)
//   if (resultArr.length > 0) {
//     answer = resultArr.sort((a,b) => {
//       if(a[1] > b[1]) return -1
//       if(a[1] < b[1]) return 1
//     })[0][0]
//   } else {
//     answer ='(None)';
//   }

//   console.log(answer)
//   return answer
// }

// 실패 1
// function solution(m, musicinfos) {
//   let answer = '';
//   for (let unit of musicinfos) {
//     let [startTime, endTime, title, musicCode] = unit.split(',');
//     let [startHour, startMin] = startTime
//       .split(':')
//       .map((v) => parseInt(v, 10));
//     let [endHour, endMin] = endTime.split(':').map((v) => parseInt(v, 10));
//     let playingTime = (endHour - startHour) * 60 + (endMin - startMin);
//     let musicTime = musicCode.length;
//     let sharpCount = musicCode.split('#').length - 1;
//     let totalCodeCount = playingTime + sharpCount;
//     let repeatNum = Math.ceil(totalCodeCount / musicTime);

//     const playingCode = musicCode.repeat(repeatNum).slice(0, totalCodeCount);
//     playingCode.split(m).length !== 1 && (answer += title);
//   }
//   console.log(answer)
//   return answer ? answer : '(None)';
// }

// #을 문자열 하나로 인식하기 때문에, playingCode에서 마지막 요소가 C#으로 들어가야 할때, totalCodeCount에 의해 C까지만 들어갈 케이스가 있음.
// m=ABC일때, playingcode='ABC#'일 경우 split으로 포함 여부를 확인하기 때문에 에러가 발생함.
