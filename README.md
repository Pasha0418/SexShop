# RandomUsersVIPER
This is the RandomUsersVIPER project that makes use of the API at https://github.com/decodealex/RandomUserNetworkService

## Build tools & versions used
- Xcode 14.1
- Swift 5
- iOS 15.0
- GitHub Actions for CI/CD

## Steps to run the app
- Run the app through Xcode with the 'RandomUsersVIPER' scheme on any iPhone device.   If this fails, try clicking File > Packages > Update to Latest Package Versions to make sure that Swift Package Manager dependencies were downloaded successfully.

## My focus:
I focused on modularity and extensibility.
- Modularity: The API is separated into a Swift Package so that it can be wholly separate from the actual app.  This allows us to test the API client and manage its releases wholly independently from the app.
- Extensibility: Anything that could be modeled as a protocol with conforming implementations was.  The reason for doing this was so that we can easily add new features to the app by either adding to the protocols, creating new protocols that the implementations could conform to, or even trading out the existing implementations of components for pretty anything that conforms to the same protocol.  Essentially, I tried to take as much of a protocol-oriented programming approach as possible.  In past projects, this has helped immensely with unit testing and refactoring.
- Object dependencies are injected, not hard coded. 
- DI injection relies on protocols, and not on objects, so we can easily inject another object (for example, for testing purposes)
- UI elements are created with reusability potential. 
- Implemented Unit tests for DataStores, JSONMapping, UserList VIPER Module (basic test cases)  
- There is basic support for Dark Mode, so feel free to take a look on a phone that's in Dark Mode as well as one that's in Light Mode.