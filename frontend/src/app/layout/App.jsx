import React, { Component, Fragment } from "react";
import { Route, Switch, withRouter } from "react-router-dom";
import { Container } from "semantic-ui-react";

import HeaderImage from "../../features/home/HeaderImage";
import RestaurantList from "../../features/restaurants/RestaurantList/RestaurantList";
import RestaurantForm from "../../features/restaurants/RestaurantForm/RestaurantForm";
import RestaurantDetails from "../../features/restaurants/RestaurantDetails/RestaurantDetails";

class App extends Component {
  render() {
    return (
      <Fragment>
        <HeaderImage />
        <Route exact path="/" component={RestaurantForm} />
        <Route
          exact
          path="/(.+)"
          render={() => (
            <Fragment>
              <Container className="main">
                <Switch key={this.props.location.key}>
                  <Route path="/list" component={RestaurantList} />
                  <Route path="/restaurant/:id" component={RestaurantDetails} />
                </Switch>
              </Container>
            </Fragment>
          )}
        />
      </Fragment>
    );
  }
}

export default withRouter(App);
