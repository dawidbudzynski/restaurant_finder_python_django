import React, {Component} from "react";
import {Card, Grid, Image} from "semantic-ui-react";

class RestaurantListItem extends Component {
  render() {
    const {restaurant} = this.props;
    return (
      <Grid>
        <Grid.Column>
          <Card centered className='restaurantCard'>
            <Image
              src={restaurant.featured_image}
              className='cardImage'
            />
            <Card.Content>

              <Card.Header>{restaurant.name}</Card.Header>
              <Card.Description>
                <span className="date">{restaurant.cuisines}</span>
              </Card.Description>
              <Card.Description className='cardDescription'>
                {restaurant.address}
              </Card.Description>
            </Card.Content>
            <Card.Content extra>
              <Card.Description>
                {restaurant.rating}
              </Card.Description>
            </Card.Content>
          </Card>
        </Grid.Column>
      </Grid>
    );
  }
}

export default RestaurantListItem;
