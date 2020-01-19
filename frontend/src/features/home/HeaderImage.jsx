import React, {Component} from "react";
import {Grid, Image} from "semantic-ui-react";


class HeaderImage extends Component {

  render() {
    return (
      <Grid>
        <div id="wrapperHeader">
          <div id="header">
            <Image
              id="header_image"
              src={"/assets/header.jpg"}
              alt="logo"/>
          </div>
        </div>
      </Grid>
    );
  }
}

export default HeaderImage;