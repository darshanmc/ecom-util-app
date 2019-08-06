from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    environment =  RadioField(label='Environment', validators=[DataRequired()], choices=[('Local', 'Local'), ('PJ', 'Project'), ('DEV', 'Dev (CLOUD)'), ('QA', 'QA (CLOUD)'), ('PROD', 'Production (CLOUD)')])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=40), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class BulkUploadForm(FlaskForm):
    schema = SelectField(label='Schema', choices=[('User', 'User'),('Organization', 'Organization'), ('Dealer', 'Dealer'), ('Dealer Order', 'Dealer Order'), ('Dealer Order Report', 'Dealer Order Report'), ('FTB Order', 'FTB Order'), ('FTB Order Report', 'FTB Order Report')])
    body = StringField('IDs')    
    execute = SubmitField(label='Execute')

class B2BBulkForm(FlaskForm):
    environment = RadioField(label='Environment', validators=[DataRequired()], choices=[('Local', 'Local'), ('PJ', 'Project'), ('QA', 'QA'), ('PROD', 'Production')])    
    schema = SelectField(label='Schema', choices=[('mappingAudit', 'Mapping Audit'),('destinationTransport', 'Destination Transport'), ('cxmlVersions', 'CXML Versions'), ('rangeDateTransaction', 'Range Date Transaction'), ('processSetupRoute', 'Process Setup Route'), ('scheduler', 'Scheduler'), ('transaction', 'Transaction'), ('rangeDateTimeTransaction','Range Date Time Transaction'), ('transTypeXRef', 'Trans Type X Ref'), ('processSetup','Process Setup'), ('sourceTransport', 'Source Transport'), ('xmlXPath', 'XML X Path')])
    execute = SubmitField(label='Execute')