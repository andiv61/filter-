import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Auth from './components/Auth';

const Routes = () => {
 return (
 <Router>
 <Switch>
 <Route path="/auth" component={Auth} />
 </Switch>
 </Router>
 );
};

export default Routes;
