import React from "react";
import { createRouter, RootRoute, Route, Outlet } from "@tanstack/react-router";
import TaskList from "./pages/TaskList";
import TaskDetail from "./pages/TaskDetail";

const rootRoute = new RootRoute({
  component: () => <Outlet />,
});

const taskListRoute = new Route({
  getParentRoute: () => rootRoute,
  path: "/",
  component: TaskList,
});

const taskDetailRoute = new Route({
  getParentRoute: () => rootRoute,
  path: "/task/$id",
  component: TaskDetail,
});

const routeTree = rootRoute.addChildren([taskListRoute, taskDetailRoute]);

export const router = createRouter({ routeTree });
