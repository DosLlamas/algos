// Review the following. Lines 3-38 are just data. The functions getUserData and getBasePizza are API calls.
// Review the task on Line 74 and complete.

// Data
const users = [
    {
        name: "Bob",
        location: "Dallas",
        birthday: "01-01-1985"
    },
    {
        name: "Bill",
        location: "Austin",
        birthday: "03-03-1981"
    },
    {
        name: "Jane",
        location: "DC",
        birthday: "10-02-1991"
    },
    {
        name: "Bonnie",
        location: "Philadelphia",
        birthday: "Thu Jan 01 1970"
    }
];

const pizzaSelection = [
    {
        name: "Pepperoni",
        toppings: ["pepperoni", "cheese"]
    },
    {
        name: "Hawaiian",
        toppings: ["pepperoni", "cheese", "pineapple"]
    },
    {
        name: "Meat Lovers",
        toppings: ["sausage", "pepperoni", "ground beef", "ham", "cheese"]
    }
];

const pricePerTopping = {
    pepperoni: 199,
    pineapple: 99,
    cheese: 159,
    "ground beef": 199,
    ham: 159,
    sausage: 199
};

//API Calls
const getUserData = (userName)=> {
    return users.find((user) => user.name === userName);
};

const getBasePizza = (pizzaSelected) => {
    return pizzaSelection.find((pizza) => pizza.name === pizzaSelected);
}; 


// Jane is now a returning customer! She would like to order some pizza again.
// This time she wants to get Meat Lovers and Hawaiian.
// It just happens that we have a 30% off deal for 2 or more pizzas.
// Construct an object that contains Jane's order

// Code after here!

/*
Steps:
1.
define function orderPizzaAgain will username, take 2 pizza names, toppingToRemove
2.
take off 30% from total price .
output of orderPizzaAgain will be an object
{
    user: {
        name,
        birthday
    },
    orderInfo: [
        pizza1: {
            name,
            toppings,
            price
        },
        pizza2:{
            name,
            toppings,
            price
        }
    ]
}
3.
define helper functions to get needed data


*/

function getNameAndBirthday(username){
    const userProfile = getUserData(username)
    return {name: userProfile.name, birthday: userProfile.birthday}
}

function getPricing(pizzas){
    const orderInfo = pizzas.map(pizza => {
            const pizzaDetails = getBasePizza(pizza)
            const pricing = pizzaDetails.toppings.reduce((total, topping) => total + pricePerTopping[topping], 0)
            return {name: pizzaDetails.name, toppings: pizzaDetails.toppings, pricing: pricing}
    })
    let totalPrice = orderInfo.reduce((sum, pizzaOrder) => sum + pizzaOrder.pricing, 0)
    if(pizzas.length >= 2) totalPrice -= totalPrice*0.3
    
    return {orderInfo: orderInfo, totalPrice: totalPrice}
}
function orderPizzaAgain(username, pizzas, toppingToRemove){
    const userProfile = getNameAndBirthday(username)
    const orderInfo = getPricing(pizzas)

    return {user:userProfile, orderInfo: orderInfo}
}

const response = orderPizzaAgain("Jane", ["Meat Lovers", "Hawaiian"])
console.log(response)


