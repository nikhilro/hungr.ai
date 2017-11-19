import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Hippo from './Hippo';


export default class Players extends Component {

  static propTypes = {
    players: PropTypes.array,
    ballCount: PropTypes.number,
    total: PropTypes.number
  };

  constructor(props) {
    super(props);

    this.state = {
      players: [],
      ballCount: 0,
      total: 0
    }
  }

  setPlayers(players) {
    this.setState({
      players: players.map(player => {
                return <Hippo
                    name={player.name}
                    score={player.score}
                  />;
              })
    });
  }

  componentWillReceiveProps(nextProps) {
    this.setState({
      players: nextProps.players,
      ballCount: nextProps.ballCount
    });
  }

  render() {
    return (
      <nav className="players">
           <div class="sidebar-header">
               <h3>Leaderboards</h3>
           </div>

           <ul class="list-unstyled components">
               <li class="active"><a href="#">Home</a></li>
               <li><a href="#">About</a></li>
               <li>
                   <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false">Pages</a>
                   <ul class="collapse list-unstyled" id="homeSubmenu">
                       <li><a href="#">Page</a></li>
                       <li><a href="#">Page</a></li>
                       <li><a href="#">Page</a></li>
                   </ul>
                </li>
               <li><a href="#">Portfolio</a></li>
               <li><a href="#">Contact</a></li>
           </ul>
       </nav>
    );
  }

}
