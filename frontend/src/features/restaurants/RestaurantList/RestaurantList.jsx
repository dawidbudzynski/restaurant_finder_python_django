import React, { Component } from "react";
import { Grid } from "semantic-ui-react";
import RestaurantListItem from "../RestaurantListItem/RestaurantListItem";

class RestaurantList extends Component {
  render() {
    const exampleData = [
      {
        id: "1",
        name: "Burger King",
        address: "Long Street"
      },
      {
        id: "2",
        name: "Good Food",
        address: "Short Street"
      },
      {
        id: "3",
        name: "McDonalds",
        address: "Nice Street"
      }
    ];
    return (
      <Grid>
        <Grid.Column width={14}>
          {exampleData.map(restaurant => (
            <RestaurantListItem key={restaurant.id} restaurant={restaurant} />
          ))}
        </Grid.Column>
      </Grid>
    );
  }
}

export default RestaurantList;
