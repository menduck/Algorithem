/**
 * HEAD => 대소문자 구별X, 사전순
 * NUMBER => 숫자 오름차순, 012=12
 * TAIL => 원래 입력 순
 */
function solution(files){
  return files.sort((a,b) => {
    const HEAD_A = a.match(/^\D+/)[0].toLowerCase()
    const HEAD_B = b.match(/^\D+/)[0].toLowerCase()

    const NUMBER_A = Number(a.match(/\d+/)[0])
    const NUMBER_B = Number(b.match(/\d+/)[0])

    // a>b 이면 return 1 이면 a->b 순으로 정렬
    if (HEAD_A > HEAD_B) return 1;
    else if(HEAD_A < HEAD_B) return -1;
    else if(NUMBER_A > NUMBER_B) return 1;
    else if(NUMBER_A < NUMBER_B) return -1;
  })
}

// solution - 실패
/**
 * 새로운 오브젝트에 HEAD와 NUMBER를 담아 조건에 맞게 정렬함.
 * 하지만 반환값은 처음 files 형태로 반환해야되기때문에 TAIL를 다시 합치고 순서에 맞게 다시 for문을 돌아야 원본형태로 정렬할 수 있음.
 * - 해결방안으로 처음부터 sort안에서 노는 방법을 생각함.
 */
function solution(files) {
  // { HEAD: 'f-', NUMBER: 5 }, ...
  const fileArray = []
  for(let file of files){
    let obj = {};
    obj.HEAD = file.match(/^\D+/)[0].toLowerCase()
    obj.NUMBER = Number(file.match(/\d+/)[0])
    fileArray.push(obj)
  }
  fileArray.sort((a,b) => {
    if(a.HEAD > b.HEAD) return 1;
    else if(a.HEAD < b.HEAD) return -1;
    else if (a.NUMBER > b.NUMBER) return 1;
    else if (a.NUMBER < b.NUMBER) return -1;
  })

  console.log(fileArray)
}

// solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(	 ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
// solution(	 ["a123a12.png"])