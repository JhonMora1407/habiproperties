CREATE TABLE user_property (
  id int(11) NOT NULL AUTO_INCREMENT,
  auth_user_id int(11) NOT NULL,
  property_id int(11) NOT NULL,
  like_property int(1) default 0,
  CONSTRAINT user_property_pk PRIMARY KEY (auth_user_id, property_id)
  CONSTRAINT user_fk FOREIGN KEY (auth_user_id) REFERENCES auth_user (id),
  CONSTRAINT property_id_fk FOREIGN KEY (property_id) REFERENCES property (id)
);


It is created in this way so that there is a client-property relationship and each time that property is consulted, 
the user will be able to indicate the vote and be related, when searching by property, since it is a numerical data, 
the number of votes could easily be added. or group by dwelling and thus obtain the votes by house