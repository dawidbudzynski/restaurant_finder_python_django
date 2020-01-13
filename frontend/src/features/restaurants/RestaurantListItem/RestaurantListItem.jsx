import React, { Component } from "react";
import { Grid, Card, Image } from "semantic-ui-react";

class RestaurantListItem extends Component {
  render() {
    const { restaurant } = this.props;
    return (
      <Grid>
        <Grid.Column>
          <Card>
            <Image
              src="https://react.semantic-ui.com/images/avatar/large/matthew.png"
              wrapped
              ui={false}
            />
            <Card.Content>
              <Card.Header>{restaurant.name}</Card.Header>
              <Card.Meta>
                <span className="date">Joined in 2015</span>
              </Card.Meta>
              <Card.Description>
                {restaurant.address}
              </Card.Description>
            </Card.Content>
          </Card>
        </Grid.Column>
      </Grid>
    );
  }
}

export default RestaurantListItem;
