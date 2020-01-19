import React, { Component } from "react";
import { Grid, Message, Card, Image, Label, Icon } from "semantic-ui-react";
import { connect } from "react-redux";

const mapState = (state, ownProps) => {
  const restaurantId = ownProps.match.params.id;

  let restaurant = {};

  if (restaurantId && state.restaurants.length > 0) {
    restaurant = state.restaurants[0].filter(
      restauranta => restauranta.id === restaurantId
    )[0];
  }

  return {
    restaurant
  };
};

class RestaurantDetails extends Component {
  render() {
    const { restaurant } = this.props;
    if (restaurant && restaurant.id) {
      return (
        <Grid>
          <Grid.Row>
            <Grid.Column>
              <Card fluid centered className="restaurantCard">
                <Image src={restaurant.featured_image} className="cardImage" />
                <Card.Content>
                  <Card.Header>{restaurant.name}</Card.Header>
                  <Card.Description>
                    <span className="date">{restaurant.cuisines}</span>
                  </Card.Description>
                  <Card.Description>{restaurant.address}</Card.Description>
                </Card.Content>
                <Card.Content extra>
                  <Card.Description>
                    <Label>
                      <Icon name="sort" />
                      Rating: {restaurant.rating}/5
                    </Label>
                  </Card.Description>
                </Card.Content>
              </Card>
            </Grid.Column>
          </Grid.Row>
        </Grid>
      );
    }
    return (
      <Grid>
        <Grid.Row>
          <Grid.Column>
            <Message warning size={"large"}>
              <Message.Header>
                Restaurant with this ID was not found
              </Message.Header>
              <p>Please go back to main page and try again.</p>
            </Message>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    );
  }
}

export default connect(mapState)(RestaurantDetails);
