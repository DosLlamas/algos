// Review the following. Lines 3-38 are just data. The functions getUserData and getBasePizza are API calls.
// Review the task on Line 74 and complete.
// Data
const users = [
    {
      name: "Bob",
      location: "Dallas",
      birthday: "01-01-1985",
    },
    {
      name: "Bill",
      location: "Austin",
      birthday: "03-03-1981",
    },
    {
      name: "Jane",
      location: "DC",
      birthday: "10-02-1991",
    },
    {
      name: "Bonnie",
      location: "Philadelphia",
      birthday: "Thu Jan 01 1970",
    },
  ];
  
  const pizzaSelection = [
    {
      name: "Pepperoni",
      toppings: ["pepperoni", "cheese"],
    },
    {
      name: "Hawaiian",
      toppings: ["pepperoni", "cheese", "pineapple"],
    },
    {
      name: "Meat Lovers",
      toppings: ["sausage", "pepperoni", "ground beef", "ham", "cheese"],
    },
  ];
  
  const pricePerTopping = {
    pepperoni: 199,
    pineapple: 99,
    cheese: 159,
    "ground beef": 199,
    ham: 159,
    sausage: 199,
  };
  
  //API Calls
  const getUserData = (userName) => {
    return new Promise((resolve, reject) => {
      const userProfile = users.find((user) => user.name === userName);
      if (userProfile) {
        resolve(userProfile);
      } else {
        reject();
      }
    });
  };
  
  const getBasePizza = (pizzaSelected) => {
    return new Promise((resolve, reject) => {
      const pizzaDetails = pizzaSelection.find(
        (pizza) => pizza.name === pizzaSelected
      );
      if (pizzaDetails) {
        resolve(pizzaDetails);
      } else {
        reject();
      }
    });
  };
  /*
  Jane's birthday is coming up and she would like to order some pizza. Construct an object
  that contains her name, birthday, and her favorite pizza, Meat Lovers, but hold the ham!! 
  Jane would also like to know how much this pizza will cost her, so please include that as well.

  Approach:
  Steps:
  1.
  Define orderSomePizza function that takes in a name, pizzaName, and topping to remove. 
  2.
  call the helper funcitons getNameAndBirthday and getPricings that use getUserData and getBaseData
  3.
  return in an object the name, birthday, pizza name, toppings, toppingRemoved and pricing

  */
  
  // Code after here!
//  using async/await method

  async function getNameAndBirthday(name){
    try {
        const userProfile = await getUserData(name)
        return {name: userProfile.name, birthday: userProfile.birthday}
    }
    catch(error){
        throw "ERROR: Did not find user. Please enter a valid username"
    }
  }
  async function getPricings(pizza, toppingToRemove){
    try {
        const pizzaData = await getBasePizza(pizza)
        const filteredToppings = pizzaData.toppings.filter(topping => topping !== toppingToRemove)
        const pricing = filteredToppings.reduce((sum, topping) => sum + pricePerTopping[topping], 0)
        return {name: pizzaData.name, toppingToRemove: toppingToRemove, toppingsOrdered: filteredToppings, pricing: pricing}
    }
    catch(error){
        throw "ERROR: Did not find pizza. Please enter a valid pizza name"
    }
  }

  async function orderSomePizza(name, pizza, toppingToRemove){
    const userProfile = await getNameAndBirthday(name)
    const pizzaData = await getPricings(pizza, toppingToRemove)
    return {user: userProfile, pizza: pizzaData}
  }
  (async () => {
    const response = await orderSomePizza("Jane", "Meat Lovers", "ham")
    console.log(response)
  })()


// answer using .then/.catch method 

// function getNameAndBirthday(name) {
//     return getUserData(name)
//       .then((userProfile) => {
//         return { name: userProfile.name, birthday: userProfile.birthday };
//       })
//       .catch(() => {
//         throw new Error("User not found");
//       });
//   }
  
//   function getPricings(pizza, toppingToRemove) {
//     return getBasePizza(pizza)
//       .then((pizzaData) => {
//         const filteredToppings = pizzaData.toppings.filter(
//           (topping) => topping !== toppingToRemove
//         );
//         const pricing = filteredToppings.reduce(
//           (sum, topping) => sum + pricePerTopping[topping],
//           0
//         );
//         return {
//           name: pizzaData.name,
//           toppingToRemove: toppingToRemove,
//           toppingsOrdered: filteredToppings,
//           pricing: pricing,
//         };
//       })
//       .catch(() => {
//         throw new Error("Pizza not found");
//       });
//   }
  
//   function orderSomePizza(name, pizza, toppingToRemove) {
//     let userProfile;
//     return getNameAndBirthday(name)
//       .then((userProfileResult) => {
//         userProfile = userProfileResult;
//         return getPricings(pizza, toppingToRemove);
//       })
//       .then((pizzaData) => {
//         return { user: userProfile, pizza: pizzaData };
//       })
//       .catch((error) => {
//         throw new Error(error.message);
//       });
//   }
  
//   // Usage
//   orderSomePizza("Jane", "Meat Lovers", "ham")
//     .then((response) => {
//       console.log(response);
//     })
//     .catch((error) => {
//       console.error(error.message);
//     });