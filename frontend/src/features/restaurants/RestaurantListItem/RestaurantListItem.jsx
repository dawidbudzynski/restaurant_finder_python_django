import React, { Component } from "react";
import { Card, Grid, Image, Button, Label, Icon } from "semantic-ui-react";
import { Link } from "react-router-dom";

class RestaurantListItem extends Component {
  render() {
    const { restaurant } = this.props;
    return (
      <Grid>
        <Grid.Column>
          <Card fluid className="restaurantCard">
            <Image src={restaurant.featured_image} className="cardImage" />
            <Card.Content>
              <Card.Header>{restaurant.name}</Card.Header>
              <Card.Description>
                <span className="date">{restaurant.cuisines}</span>
              </Card.Description>
              <Card.Description>
                {restaurant.address}
              </Card.Description>
            </Card.Content>
            <Card.Content extra>
              <Card.Description>
                <Label>
                  <Icon name="sort" />Rating: {restaurant.rating}/5
                </Label>
              </Card.Description>
            </Card.Content>
            <Button
              as={Link}
              to={`/restaurant/${restaurant.id}`}
              color="green"
              content="View"
            />
          </Card>
        </Grid.Column>
      </Grid>
    );
  }
}

export default RestaurantListItem;
