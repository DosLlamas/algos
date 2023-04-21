/*
Write a component that makes an API Call to /api/v1/items/ and displays the results. Here is the shape of the API response:
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
*/

