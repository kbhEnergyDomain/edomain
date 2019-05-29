db.createUser({
      user: "admin",
      pwd: "appDeveloper",
      roles: [
                { role: "userAdminAnyDatabase", db: "admin" },
                { role: "readWriteAnyDatabase", db: "admin" },
                { role: "dbAdminAnyDatabase",   db: "admin" }
             ]
  });

  db.createUser({
      user: "user1",
      pwd: "appDeveloper",
      roles: [
                { role: "userAdmin", db: "sampledb" },
                { role: "dbAdmin",   db: "sampledb" },
                { role: "readWrite", db: "sampledb" }
             ]
  });