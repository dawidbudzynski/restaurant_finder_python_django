import React, {Component} from "react";
import axios from "axios";
import {Grid} from "semantic-ui-react";
import RestaurantListItem from "../RestaurantListItem/RestaurantListItem";

class RestaurantList extends Component {
  state = {
    restaurants: []
  };

  componentDidMount() {
    axios.get(`http://localhost:8000/pl/api/restaurant-list/`).then(res => {
      const restaurants = res.data;
      this.setState({restaurants});
    });
  }

  render() {
    const {restaurants} = this.state;
    return (
      <Grid>
        <Grid.Column width={14}>
          {restaurants.map(restaurant => (
            <RestaurantListItem key={restaurant.id} restaurant={restaurant}/>
          ))}
        </Grid.Column>
      </Grid>
    );
  }
}

export default RestaurantList;
