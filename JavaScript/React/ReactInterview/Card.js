import React from 'react'

const Card = ({ item, key, handleDelete }) => {
  return (
    <div style={{border: "1px solid red"}}>
        <h2>{item.name}</h2>
        {/* The "image-url" property cannot be access with dot notation due to the hyphen.
            Must use bracket notation as a string.
        */}
        <img src={item["image-url"]} />
        <p>{item.description}</p>
        <button onClick={() => handleDelete(key)}>Delete card</button>
    </div>
  )
}
export default Card;