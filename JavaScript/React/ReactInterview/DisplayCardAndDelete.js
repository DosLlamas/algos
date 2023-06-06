/*
Question:

Write a component that makes an API Call to /api/v1/items/ and displays the results.
Here is the shape of the API response:
[
  {
    "id": "sddfoush9r447w-343-dsf4-sdfwe4t65e6",
    "description": "See some interestin info about Item 1",
    "image-url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fnews%2Fworld-us-canada-37493165&psig=AOvVaw2awenud8C1LjSfe5kFhICK&ust=1682039630908000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNj8poekt_4CFQAAAAAdAAAAABAE",
    "name": "Item 1",
    "owner-id": "asdgo4ww4y9-3w4efw-few44wef-efds48w9"
  }
]

1. 
Each item should be displayed in a "card" or "box" displaying the name, description and image of that item.
2.
Add a button for each card that deletes the card from the database and front end? 
Use this endpoint: DELETE /api/v1/item/{id}/

My solution:
Steps:
1.
Import useEffect and useState and create component
2.
Make fetch and hold data in items useState array
3.
Create second array, Map through useState array creating JSX cards for each
4.
Create Card component to display info for each card
5.
Create button to invoke an onDelete for each card
6. 
Filter through cards to remove item.id that was clicked from state and
fetch delete request to api for that item.id 
*/


import React, { useEffect, useState} from "react"
import Card from "./Card.js"


const DisplayCardAndDelete = () => {

    const [items, setItems ] = useState([])
    useEffect(() => {
        fetch('/api/v1/items/')
        .then(r => r.json())
        .then(data => setItems(data))
    }, [])

    const handleDelete = (id) => {
        fetch(`/api/v1/item/${id}/`)
        .then(() => {
            setItems(items.filter(item => item.id !== id))
        })
    }
    const renderCards = items.map(item => {
        return (
            <Card item={item} key={item.id} handleDelete={handleDelete}/>
        )
    })
    return (
        {renderCards}
    )
}
export default DisplayCardAndDelete;



/*
Important takeways from this problem:
1. 
Understand how to manage useEffect and useState to hold data from an API call
2.
Understand how to make GET and DELETE fetch requests to an API, 
not forgetting the dependecy array for the useEffect.
3.
Understand the life-cycle of a react component to update
state when an item is deleted from the DOM
4. 
Understand that you should renderJSX as a new array that has been mapped from your data
so you're able to dynamically filter out deleted items
5. 
Understand how to use callback functions as events to pass data
to and from a parent component
*/
