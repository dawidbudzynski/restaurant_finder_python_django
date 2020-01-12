import React, {Component} from "react";
import {Grid} from "semantic-ui-react";
import RestaurantForm from '../restaurants/RestaurantForm/RestaurantForm'
import HeaderImage from "./HeaderImage";


class HomePage extends Component {

  render() {
    return (
      <Grid>
        <Grid.Column width={16}>
          <HeaderImage/>
          <RestaurantForm/>
        </Grid.Column>
      </Grid>
    );
  }
}

export default HomePage;

