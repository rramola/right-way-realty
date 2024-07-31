import React, { useEffect, useState } from "react";
import axios from "axios";

function Properties() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/properties/")
      .then((response) => {
        setProperties(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div>
      <h1>Properties</h1>
      {properties.length > 0 ? (
        <ul>
          {properties.map((property) => (
            <li key={property.id}>
              <h2>{property.title}</h2>
              <p>{property.description}</p>
              <p>Price: ${property.price}</p>
              <p>Address: {property.address}</p>
              <p>Bedrooms: {property.bedrooms}</p>
              <p>Bathrooms: {property.bathrooms}</p>
              <p>Square Footage: {property.sqft}</p>
              {property.images.length > 0 && (
                <div>
                  {property.images.map((image, index) => (
                    <img
                      key={index}
                      src={`http://127.0.0.1:8000${image.image}`}
                      alt={`Image of ${property.title}`}
                      style={{ width: "200px", height: "auto", margin: "10px" }}
                    />
                  ))}
                </div>
              )}
            </li>
          ))}
        </ul>
      ) : (
        <p>No properties available.</p>
      )}
    </div>
  );
}

export default Properties;
