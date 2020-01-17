import React, { Component } from "react";
import { connect } from "react-redux";
import { reduxForm, Field } from "redux-form";
import { combineValidators, isRequired } from "revalidate";
import { Segment, Form, Button, Grid, Header } from "semantic-ui-react";
import cuid from "cuid";
import { saveSearchParams } from "../../../redux/searchParams/searchParamsActions";
import TextInput from "../../../app/common/form/TextInput";

const mapState = (state, ownProps) => {
  return {}
};

const actions = {
  saveSearchParams
};

const validate = combineValidators({
  city: isRequired({ message: "The field is required" }),
  street: isRequired({ message: "The field is required" })
});

class RestaurantForm extends Component {

  onFormSubmit = values => {
    const searchParams = {
        ...values,
        id: cuid(),
      };
    this.props.saveSearchParams(searchParams);
    this.props.history.push("/list");
  };

  render() {
    const {
      invalid,
      submitting,
      prestine
    } = this.props;
    return (
      <Grid centered>
        <Grid.Column width={14} id="form">
          <Segment>
            <Header sub color="teal" content="Restaurant Address" />
            <Form
              onSubmit={this.props.handleSubmit(this.onFormSubmit)}
              autoComplete="off"
            >
              <Field name="city" component={TextInput} placeholder={"City"} />
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
              <Button type="button">
                Clear
              </Button>
            </Form>
          </Segment>
        </Grid.Column>
      </Grid>
    );
  }
}

export default connect(
  mapState,
  actions
)(reduxForm({ form: "restaurantForm", validate })(RestaurantForm));
