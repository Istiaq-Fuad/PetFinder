import React, { useEffect, useState } from "react";
import axiosInstance from "../axios";
import { useParams } from "react-router-dom";
import { jwtDecode } from "jwt-decode";

function SinglePost() {
  const { petID } = useParams();
  const [pet, setPet] = useState([]);
  let access_token = localStorage.getItem("access_token");
  // console.log(access_token);

  if (access_token !== null) {
    const userId = jwtDecode(access_token)?.user_id;
    console.log(userId);
  }

  useEffect(() => {
    axiosInstance.get(`pets/${petID}`).then((res) => {
      const singlePet = res.data;
      setPet(singlePet);
      // console.log(res.data);
    });
  }, [petID, setPet]);
  return (
    <div>
      <div>{pet.name}</div>
      <div>{pet.species}</div>
      <div>{pet.breed}</div>

      <button>application</button>
    </div>
  );
}

export default SinglePost;
