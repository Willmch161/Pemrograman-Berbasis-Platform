function convertTemp(C) {
    return {
        Reaumur: (4 / 5) * C,
        Fahrenheit: (9 / 5) * C + 32,
        Kelvin: C + 273.15
    };
}
let temp = convertTemp(25);
console.log("3. Temperature →", temp);