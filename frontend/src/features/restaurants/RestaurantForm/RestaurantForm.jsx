import React, { Component } from "react";
import { connect } from "react-redux";
import { reduxForm, Field } from "redux-form";
import {
  combineValidators,
  isRequired,
} from "revalidate";
import { Segment, Form, Button, Grid, Header } from "semantic-ui-react";
import { searchRestaurants } from "../eventActions";
import TextInput from "../../../app/common/form/TextInput";

const mapState = (state, ownProps) => {
  let restaurant = {};
  return {
    initialValues: restaurant
  };
};

const actions = {
  searchRestaurants
};

const validate = combineValidators({
  city: isRequired({ message: "The field is required" }),
  street: isRequired({ message: "The field is required" }),
});

class RestaurantForm extends Component {
  state = { ...this.props.event };

  onFormSubmit = values => {
      const restaurantData = {
        ...values
      };
      this.props.searchRestaurants(restaurantData);
  };

  render() {
    const {
      history,
      initialValues,
      invalid,
      submitting,
      prestine
    } = this.props;
    return (
      <Grid>
          <Segment>
            <Header sub color="teal" content="Restaurant Address" />
            <Form
              onSubmit={this.props.handleSubmit(this.onFormSubmit)}
              autoComplete="off"
            >
              <Field
                name="city"
                component={TextInput}
                placeholder={"City"}
              />
               <Field
                name="street"
                component={TextInput}
                placeholder={"Street"}
              />
              <Button
                disabled={invalid || submitting || prestine}
                positive
                type="submit"
              >
                Submit
              </Button>
              <Button
                onClick={
                  initialValues.id
                    ? () => history.push(`/events/${initialValues.id}`)
                    : () => history.push("/events/")
                }
                type="button"
              >
                Cancel
              </Button>
            </Form>
          </Segment>
      </Grid>
    );
  }
}

export default connect(
  mapState,
  actions
)(reduxForm({ form: "restaurantForm", validate })(RestaurantForm));
