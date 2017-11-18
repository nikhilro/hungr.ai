import React, { Component } from 'react';
import {List, ListItem} from 'material-ui/List';
import Divider from 'material-ui/Divider';

export default class Sidebar extends React.Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }

  handleToggle = () => this.setState({
    open: !this.state.open
  });

  handleClose = () => this.setState({ open: false });

  render() {
    return (
      <div className="sidebar">
        <List>
          <ListItem primaryText="Item 1" />
          <ListItem primaryText="Item 2" />
          <ListItem primaryText="Item 3" />
          <Divider inset={true} />
          <ListItem primaryText="Item 4" />
          <ListItem primaryText="Item 5" />
          <ListItem primaryText="Item 6" />
        </List>
      </div>
    );
  }
}
