import React, {Component} from "react";
import {Grid} from "semantic-ui-react";


class HomePage extends Component {

  render() {
    return (
      <Grid>
        <div id="wrapperHeader">
          <div id="header">
            <img
              id="header_image"
              src={"/assets/header.jpg"}
              alt="logo"/>
          </div>
        </div>
      </Grid>
    );
  }
}

export default HomePage;

