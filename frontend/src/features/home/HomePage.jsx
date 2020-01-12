import React, {Component} from "react";
import {Grid, Image} from "semantic-ui-react";
import RestaurantForm from '../restaurants/RestaurantForm/RestaurantForm'


class HomePage extends Component {

  render() {
    return (
      <Grid>
        <div id="wrapperHeader">
          <div id="header">
            <Image
              id="header_image"
              src={"/assets/header.jpg"}
              alt="logo"/>
          </div>
        </div>
        <RestaurantForm/>
      </Grid>
    );
  }
}

export default HomePage;

