const input = "금성"

const ko = ["수성","금성","지구","화성","목성","토성","천왕성","해왕성"];
const eng =['Mercury','Venus','Earth','Mars','Jupiter', 'Saturn', 'Uranus','Neptune']

const inputIndex = ko.indexOf(input)
console.log(eng[inputIndex])

//추가 코드
//object로 이용해서 풀어보기

const planets = {
	'수성' : 'Mercury',
	'금성' : 'Venus',
	'지구' : 'Earth',
	'화성' : 'Mars',
	'목성' : 'Jupiter',
	'토성' : 'Saturn',
	'천왕성' : 'Uranus',
	'해왕성' : 'Neptune',
};

const planetName = "천왕성"
console.log(planets[planetName])