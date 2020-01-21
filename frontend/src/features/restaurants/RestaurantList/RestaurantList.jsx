import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { Grid, Segment, Dimmer, Loader, Image } from "semantic-ui-react";
import RestaurantListItem from "../RestaurantListItem/RestaurantListItem";
import { saveRestaurantList } from "../../../redux/restaurants/restaurantsActions";

const mapState = state => ({
  searchParams: state.searchParams,
  restaurants: state.restaurants
});

const actions = {
  saveRestaurantList
};

class RestaurantList extends Component {
  state = {
    restaurants: []
  };

  componentDidMount() {
    const searchParams = this.props.searchParams;
    if (searchParams && searchParams.length > 0) {
      const { city, street } = searchParams[0];
      try {
        axios
          .get(`http://localhost:8000/pl/api/restaurant-list/${city}/${street}`)
          .then(res => {
            const response = res.data;
            if (response && response.length > 0) {
              this.props.saveRestaurantList(response);
            }
          });
      } catch (error) {
        // todo doesn't catch errors
        console.log(error);
      }
    }
  }

  render() {
    let restaurants = [];
    if (this.props.restaurants && this.props.restaurants.length > 0) {
      restaurants = this.props.restaurants;
      return (
        <Grid>
          <Grid.Row>
            {restaurants.map(restaurant => (
              <Grid.Column key={restaurant.id} width={16}>
                <RestaurantListItem restaurant={restaurant} />
              </Grid.Column>
            ))}
          </Grid.Row>
        </Grid>
      );
    }
    return (
      <Grid>
        <Grid.Row>
          <Grid.Column>
            <Segment>
              <Dimmer active>
                <Loader indeterminate>Looking for nearby restaurants</Loader>
              </Dimmer>
              <Image src="https://react.semantic-ui.com/images/wireframe/short-paragraph.png" />
            </Segment>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    );
  }
}

export default connect(mapState, actions)(RestaurantList);
