=====================
FletNavigator V2.2.3
=====================

.. image :: https://github.com/xzripper/flet_navigator/raw/main/example2.gif
   :width: 500

FletNavigator & `FletReStyle <https://github.com/xzripper/flet_restyle>`_

Simple and fast navigator (router) for Flet (Python) that allows you to create multi-page applications!

Click `here <https://github.com/xzripper/flet_navigator/blob/main/flet-navigator-docs.md>`_ for documentation.

Using Example:

.. code :: python

   from flet import app, Page

   from flet_navigator import VirtualFletNavigator, PageData, ROUTE_404


   def main_page(pg: PageData) -> None:
      ... # Main page content.

   def second_page(pg: PageData) -> None:
      ... # Second page content.

   def route_404(pg: PageData) -> None:
      ... # 404 Page Content.

   def main(page: Page) -> None:
      # Initialize navigator.
      flet_navigator = VirtualFletNavigator(
         {
               '/': main_page, # Main page route.
               'second_page': second_page, # Second page route.
               ROUTE_404: route_404 # 404 page route.
         }, lambda route: print(f'Route changed!: {route}') # Route change handler (optional).
      )

      flet_navigator.render(page) # Render current page.

   app(target=main)

.. image :: https://raw.githubusercontent.com/xzripper/flet_navigator/main/example.gif
   :width: 400

(Deprecated Example GIF).

See the difference between `VirtualFletNavigator` and `FletNavigator`, and more `here <https://github.com/xzripper/flet_navigator/blob/main/flet-navigator-docs.md>`_ (<- documentation).

-----------------------------------------------

   FletNavigator V2.2.3
