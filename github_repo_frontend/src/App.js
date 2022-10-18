import "./styles.css";
import React from "react"

class App extends React.Component {
  constructor(props) {
  super(props);
  this.state = {
    usernameList: [],
    username: "",
    repos: [],
    };
}

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/usernames');
      const usernameList = await res.json();
      this.setState({usernameList: usernameList});
    } catch (e) {
      console.log(e);
  }
  }

  async getRepos(username) {
    try {
      const res = await fetch('http://127.0.0.1:8000/repos/' + username);
      const reposList = await res.json();
      this.setState({repos: reposList});
    } catch (e) {
      console.log(e);
  }
  };

  async handleOnChange(position) {
   this.setState({username: this.state.usernameList[position]});
   this.getRepos(this.state.usernameList[position]);
 };

  render() {
    return (
      <div className="App">
      <h3>GitHub Repository</h3>

      <ul className="contents">
        <div className="username">Usernames:</div>
        {this.state.usernameList.map((name, index) => {
          return (
            <li key={index}>
              <div className="usernames-list-item">
                <div className="username_button">
                  <input
                    type="button"
                    id={`custom-checkbox-${index}`}
                    name={name}
                    value={name}
                    onClick={() => this.handleOnChange(index)}
                  />
                </div>
              </div>
            </li>
          );
        })}
        <div className="username">Selected username:</div>
        <div className="username_display">{this.state.username}</div>
        <div className="repository_list">Repository List:</div>
        {this.state.repos.map((name, index) => {
          return (
            <li key={index}>
              <div className="repos-list-item">
                  <div>{name}</div>
              </div>
            </li>
          );
        })}
      </ul>
    </div>
    )
  }
}

export default App;
