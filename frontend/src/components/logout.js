import React, { useEffect } from "react";
import axiosInstance from "../axios";
import { useHistory } from "react-router-dom";
import useLogin from "../stores/loginStore";

export default function SignUp() {
  const history = useHistory();
  const setLoginState = useLogin((state) => state.setLoginState);

  useEffect(() => {
    const response = axiosInstance.post("user/logout/blacklist/", {
      refresh_token: localStorage.getItem("refresh_token"),
    });
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    axiosInstance.defaults.headers["Authorization"] = null;
    setLoginState(false);
    history.push("/login");
  });
  return <div>Logout</div>;
}
