import React, { Component } from "react";
import { Grid, Message, Card, Image, Label, Icon } from "semantic-ui-react";
import { connect } from "react-redux";

const mapState = (state, ownProps) => {
  const restaurantId = ownProps.match.params.id;

  let selectedRestaurant = {};

  if (restaurantId && state.restaurants.length > 0) {
    selectedRestaurant = state.restaurants.filter(
      restaurant => restaurant.id === restaurantId
    )[0];
  }

  return {
    selectedRestaurant
  };
};

class RestaurantDetails extends Component {
  render() {
    const { selectedRestaurant } = this.props;
    const restaurantImage = selectedRestaurant.featured_image ? selectedRestaurant.featured_image : '/assets/defaultImage.jpg';
    if (selectedRestaurant && selectedRestaurant.id) {
      return (
        <Grid>
          <Grid.Row>
            <Grid.Column>
              <Card fluid centered className="restaurantCard">
                <Image src={restaurantImage} className="cardImage" />
                <Card.Content>
                  <Card.Header>{selectedRestaurant.name}</Card.Header>
                  <Card.Description>
                    <span className="date">{selectedRestaurant.cuisines}</span>
                  </Card.Description>
                  <Card.Description>{selectedRestaurant.address}</Card.Description>
                </Card.Content>
                <Card.Content extra>
                  <Card.Description>
                    <Label>
                      <Icon name="sort" />
                      Rating: {selectedRestaurant.rating}/5
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
