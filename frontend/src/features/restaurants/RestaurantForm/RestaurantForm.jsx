import React, { Component } from "react";
import { connect } from "react-redux";
import { reduxForm, Field } from "redux-form";
import { combineValidators, isRequired } from "revalidate";
import { Form, Button, Grid } from "semantic-ui-react";
import cuid from "cuid";
import { saveSearchParams } from "../../../redux/searchParams/searchParamsActions";
import TextInput from "../../../app/common/form/TextInput";

const mapState = (state, ownProps) => {
  return {};
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
      id: cuid()
    };
    this.props.saveSearchParams(searchParams);
    this.props.history.push("/list");
  };

  clearForm = () => {
    this.props.reset();
  };

  render() {
    const { invalid, submitting, prestine } = this.props;
    return (
      <Grid centered>
        <Grid.Column width={14}>
          <Form
            onSubmit={this.props.handleSubmit(this.onFormSubmit)}
            autoComplete="on"
          >
            <Form.Group widths={"equal"}>
              <Field name="city" component={TextInput} placeholder={"City"} />
              <Field
                name="street"
                component={TextInput}
                placeholder={"Street"}
              />
            </Form.Group>
            <Button.Group widths={7}>
              <Button
                disabled={invalid || submitting || prestine}
                positive
                type="submit"
              >
                Search
              </Button>
              <Button.Or />
              <Button type="button" onClick={this.clearForm}>
                Clear
              </Button>
            </Button.Group>
          </Form>
        </Grid.Column>
      </Grid>
    );
  }
}

export default connect(
  mapState,
  actions
)(reduxForm({ form: "restaurantForm", validate })(RestaurantForm));
