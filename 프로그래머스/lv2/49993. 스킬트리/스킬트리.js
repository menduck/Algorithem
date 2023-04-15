function solution(skill, skill_trees){
  let result = 0

  for (let skill_tree of skill_trees){
    const skill_tree_array = skill_tree.split('')
    result += isInOrder(skill, skill_tree_array)
  }
  return result
}
// ('CBDA',[ 'C', 'B', 'A' ])
function isInOrder(skill, skill_tree_array){
  const order = skill_tree_array.map(v=> skill.indexOf(v)).filter(v=> v !== -1) 
  const rightOrder = [...Array(order.length).keys()] // [0,1,2]
  return order.filter((v,idx) => rightOrder[idx] === v).length === order.length ? 1 : 0
}


console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


// solution - 실패

// function solution(skill, skill_trees){
//   const skills = skill.split('');
//   let result = 0

//   for (let skill_tree of skill_trees){
//     result += isInOrder(skills, skill_tree)
//   }
//   return result
// }

// function isInOrder(skills, skill_tree){
//   let skillNumber = skill_tree.indexOf(skills[0]);
//   if (skillNumber === -1) return 0;
//   let flag = false;
//   for (let i = 1; i<skills.length; i++){
//     if (skillNumber < skill_tree.indexOf(skills[i])) {
//       skillNumber = skill_tree.indexOf(skills[i])
//       flag = true
//     } else {
//         break
//     }
//   }
//   return flag ? 1 : 0
// }
// solution - 실패
// function solution(skill, skill_trees) {
//   let result = 0
//   const skillArray = skill.split('')
//   for(skill_tree of skill_trees.filter(v => v.includes(skill[0]))){
//       const treeArray = skill_tree.split('')
//       const index_skill = skillArray.map(v => treeArray.indexOf(v))
//       for(let i = 0; i<index_skill.length -1 ;i++){
//         if (index_skill[i] !== -1 && index_skill[i+1] - index_skill[i] === 1 ) result += 1
//       }
//   }
//   return result
// }