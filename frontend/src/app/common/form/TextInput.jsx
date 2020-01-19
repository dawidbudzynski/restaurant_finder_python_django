import React from "react";
import { Form, Label } from "semantic-ui-react";

const TextInput = ({
  input,
  type,
  placeholder,
  width,
  meta: { touched, error }
}) => {
  return (
    <Form.Field error={touched && !!error}>
      <input {...input} placeholder={placeholder} type={type} width={width} />
      {touched && error && (
        <Label basic color="red">
          {error}
        </Label>
      )}
    </Form.Field>
  );
};

export default TextInput;
