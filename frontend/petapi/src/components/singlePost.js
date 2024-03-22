import React, { useEffect, useState } from "react";
import axiosInstance from "../axios";
import { useParams } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import { Button, Box } from "@material-ui/core";

function SinglePost() {
  const { petId } = useParams();
  const [pet, setPet] = useState([]);
  const [buttonText, setButtonText] = useState("Request adoption");
  const [buttonDisable, setButtonDisable] = useState(false);
  let access_token = localStorage.getItem("access_token");
  // console.log(access_token);
  let userId;
  if (access_token !== null) {
    userId = jwtDecode(access_token)?.user_id;
    // console.log(userId);
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    axiosInstance
      .post(`applications/`, {
        pet: petId,
        // user: userId,
        // password: formData.password,
      })
      .then((res) => {
        setButtonText("request submitted");
        setButtonDisable(true);
      })
      .catch((e) => console.log(e));
  };

  useEffect(() => {
    axiosInstance.get(`pets/${petId}`).then((res) => {
      const singlePet = res.data;
      setPet(singlePet);
      // console.log(res.data);
    });

    axiosInstance.get("applications").then((res) => {
      const applications = res.data;
      const matchedApplication = applications.filter(
        (application) =>
          application.user === userId && application.pet === petId
      );
      if (matchedApplication.length !== 0) {
        setButtonText("request submitted");
        setButtonDisable(true);
      }
    });
  }, [petId, userId, setPet]);

  return (
    <Box>
      <div>{pet.name}</div>
      <div>{pet.species}</div>
      <div>{pet.breed}</div>

      {/* <Button
        disabled={buttonDisable}
        type="submit"
        variant="contained"
        color="primary"
        onClick={handleSubmit}
      >
        {buttonText}
      </Button> */}
    </Box>
  );
}

export default SinglePost;
