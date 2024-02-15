const message = 'Fuck you'
let changable = "Pack hier später was hin"

let person = {
    age: 71,
    name: "Zinedine",
    Aussage: "Da sind Witherskellete"
};

console.log(person);

person.name = 'Fabian'

console.log(person)

function load(input){
    let namen = []
    namen[0] = "Zin";
    namen[1] = "Fabian";
    namen[2] = "Frederik";
    namen[3] = "Tobias";
    namen[4] = "Ricardo";
    namen[5] = input;
    return namen;
}

names = load("Daniel");
console.log(names);

//https://www.youtube.com/watch?v=DABVLJjnVUs