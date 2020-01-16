import React, {Component} from "react";
import {connect} from "react-redux";
import axios from "axios";
import {Grid} from "semantic-ui-react";
import RestaurantListItem from "../RestaurantListItem/RestaurantListItem";
import {saveRestaurantList} from "../../../redux/restaurants/restaurantsActions";

const mapState = state => ({
  searchParams: state.searchParams
});

const actions = {
  saveRestaurantList
};

class RestaurantList extends Component {
  state = {
    restaurants: []
  };


  componentDidMount() {
    const {searchParams} = this.props;
    if (searchParams) {
      const {city, street} = searchParams[0];
      axios.get(`http://localhost:8000/pl/api/restaurant-list/${city}/${street}`).then(res => {
        const restaurants = res.data;
        // this.props.saveRestaurantList(restaurants);
        this.setState({restaurants});
      });
    }

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

export default connect(mapState, actions)(RestaurantList);
