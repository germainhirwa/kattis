var restaurants = parseInt(readline()); // the number of restaurants
let exists = false;
for (let i = 0; i < restaurants; i++) {
    let menus = parseInt(readline()); // the number of menus
    let name = readline();
    let peas = false;
    let pancakes = false;

    for (let j = 0; j < menus; j++) {
        let food = readline();
        if (food === "pea soup") {
            peas = true;
        } else if (food === "pancakes") {
            pancakes = true;
        }
    }

    if (peas && pancakes) {
        console.log(name);
        exists = true;
        break;
    }
}

if (!exists) {
    console.log("Anywhere is fine I guess");
}