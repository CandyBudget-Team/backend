# backend
The backend database and api for the ui-ux client.

We need to provide an API for logic to the client to allow the parents to set virtual budgets, follow each AU history and control the account's health.

We need a cron job for making the computations and synching our features in our database. This way, each user has their parameters up to date. Alternatively we can make the user compute these themselves. Either the primary account holder will trigger computation for all the account users or a user will trigger the computation. This way we do not lose computation time by running the cron job all the time. A time of last update should be used to reduce the amount of data to take into account (transactions).

We should focus on building a scalable and extensible budget model with different rankings. For example we have the saving model and the wise spending model. We can add the planing model for the parent to rank them too in how they doing compared to historical data.
