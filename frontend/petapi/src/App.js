import React, { useEffect, useState } from "react";
import "./App.css";
import Posts from "./components/posts";
import PostLoadingComponent from "./components/postLoading";
import axiosInstance from "./axios";
import useLogin from "./stores/loginStore";
import Button from "@material-ui/core/Button";
import "./App.css";
import { NavLink } from "react-router-dom";

function App() {
  const PostLoading = PostLoadingComponent(Posts);
  const [appState, setAppState] = useState({
    loading: true,
    posts: null,
  });

  const loggedIn = useLogin((state) => state.loggedIn);

  useEffect(() => {
    axiosInstance.get("pets/").then((res) => {
      const allPosts = res.data;
      setAppState({ loading: false, posts: allPosts });
      // console.log(res.data);
    });
  }, []);

  return (
    <div className="App">
      <div className="adoption-button">
        {loggedIn && (
          <Button variant="contained" color="primary" to="/create-post" component={NavLink}>
            Post for adoption
          </Button>
        )}
      </div>
      <PostLoading isLoading={appState.loading} posts={appState.posts} />
    </div>
  );
}
export default App;
