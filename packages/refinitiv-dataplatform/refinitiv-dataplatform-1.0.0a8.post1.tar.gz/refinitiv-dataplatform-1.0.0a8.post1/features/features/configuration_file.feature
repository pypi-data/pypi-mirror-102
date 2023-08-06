Feature: Configuration file

  Background: Clean up the environment
    Given Old config files deleted
    Given Configuration reloaded

  Scenario: Configuration values saved
    Given I have been using the Library as dependency in my project
    When I create the 'rdplibconfig.prod.json' file in the project root directory
    And I set dataplatform env to 'prod' (using 'RDPLIB_ENV')
    Then Configuration values saved at 'rdplibconfig.prod.json' are used in appropriate places of Library

  Scenario: Default configuration
    Given I have been using the Library as dependency in my project
    When I don't have the 'rdplibconfig.feat1.json' configuration file at the project root directory
    And I set dataplatform env to 'feat1' (using 'RDPLIB_ENV')
    Then Default configuration (hardcoded in the Library) is used
  #  Note. The lowest priority config file

  Scenario: The individual default value is overridden
    Given I have been using the Library as dependency in my project
    When I create the 'rdplibconfig.feat1.json' file in the project root directory
    And I write there only one parameter from a list of parameters
    And I set dataplatform env to 'feat1' (using 'RDPLIB_ENV')
    Then The individual default value is overridden. All other values come from the default config (hardcoded in the Library config file).

  Scenario: Config file in <project_root> folder is used
    Given I have been using the Library as dependency in my project
    When I create the 'rdplibconfig.beta.json' configuration file in directory within the project ('<project_root>/example/folder')
    And I set dataplatform env to '<project_root>/example/folder' (using 'RDPLIB_ENV_DIR')
    And I set dataplatform env to 'beta' (using 'RDPLIB_ENV')
    Then Config file 'rdplibconfig.beta.json' in folder '<project_root>/example/folder' is used.
  #  Note. Project Working Dir (pwd) configuration file has the highest priority

  Scenario: Config file in <USER_HOME> folder is used
    Given I have been using the Library as dependency in my project
    When I create the 'rdplibconfig.prod.json' configuration file in the User's Home directory
    And I set dataplatform env to 'prod' (using 'RDPLIB_ENV')
    Then Config file 'rdplibconfig.prod.json' in folder '<USER_HOME>' is used.
  #  Note. User's Home (Unix $HOME, Windows %HOMEPATH%) configuration file has lower priority then pwd config file.

  Scenario: A new configuration is applied
    Given I have been using the Library as dependency in my project
    And I create the 'rdplibconfig.feat.json' file in the project root directory
    And I set dataplatform env to 'feat' (using 'RDPLIB_ENV')
    When I enable watch mode
    And I change/add/remove configuration file
    Then A new configuration is applied 'on the fly' while maintaining priority

  Scenario: Appropriate value from the current config file
    Given I have been using the Library as dependency in my project
    And I create the 'rdplibconfig.feat.json' file in the project root directory
    And I set dataplatform env to 'feat' (using 'RDPLIB_ENV')
    When I use a template string in the format '${key1:key2:key3}'
    Then Appropriate value from the current config file 'key1.key2.key3' will be applied instead of template

  Scenario: If key sequence does not exist
    Given I have been using the Library as dependency in my project
    And I create the 'rdplibconfig.feat.json' file in the project root directory
    And I set dataplatform env to 'feat' (using 'RDPLIB_ENV')
    When I use a template string for not exist path in the format '${key1:key2:key3:key4}'
    Then Template string will not be replaced (value is a string '${key1:key2:key3:key4}')

  Scenario: Appropriate value from the environment variables
    Given I have been using the Library as dependency in my project
    And I create the 'rdplibconfig.feat.json' file in the project root directory
    And I set dataplatform env to 'feat' (using 'RDPLIB_ENV')
    When I use a template string for get from environment in the format '${ENV_VARIABLE}'
    Then Appropriate value from the environment variables 'ENV_VARIABLE' will be applied instead of template

  Scenario: If no such env variable
    Given I have been using the Library as dependency in my project
    And I create the 'rdplibconfig.feat.json' file in the project root directory
    And I set dataplatform env to 'feat' (using 'RDPLIB_ENV')
    When I use a template string for not exist environment in the format '${ENV_VARIABLE}'
    Then No such env variable - looking for 'ENV_VARIABLE' field withing the config file to replace the template

# config-change-notifications-enabled

  Scenario: Set true for receive notifications
    Given I have a config file in my project
    When I set "config-change-notifications-enabled" setting to random value ("t", "true", "y", "yes", "on", "1")
    Then I receive notifications about changes in configuration file

  Scenario: Set false for avoid notifications
    Given I have a config file in my project
    When I set "config-change-notifications-enabled" setting to random value ("f", "false", "n", "no", "off", "0", "")
    Then I do not receive any notifications about changes in the configuration files

    #This test scenario needs the requirements clarification
  @skip
  Scenario: Set string-value for receive notifications
    Given I have a config file in my project
    When I set "config-change-notifications-enabled" setting to random value ("string", "0", "fals", "hi")
    Then I receive notifications about changes in configuration file

  Scenario: Receive single notification event about each change
    Given I have a config file in my project
    When I set "config-change-notifications-enabled" setting to "true"
    Then I receive single notification event about each change in the configuration file

  Scenario: Change settings at an intermediate level
    Given I have a config file in my project (watch mode is enabled)
    When I change settings at an intermediate level that does not affect the final configuration
    Then I don't receive an event notification

  Scenario: Receive an event notification with the final object
    Given I have a config file in my project (watch mode is enabled)
    And I have the same settings list in the PWD and USER HOMEDIR config files with different values (e.g. PWD logs.level:debug, USER HOMEDIR logs.level:info => final logs.level:debug)
    When I delete PWD config file
    Then I receive an event notification with the final object logs.level:info and the source that has been physically modified (PWD).

# logs

  Scenario: Appropriate level of log
    Given I have a config file in my project
    When I set "logs.level" setting to random value (trace, debug, info, warn, error, silent)
    Then Appropriate level for project logger is applied.

  Scenario: Verify that logs file name was changed
    Given I have a config file in my project
    When I set "logs.transports.file.name" setting to "test_log_file.log"
    Then "test_log_file.log" is used as file-name config value.

  Scenario: The corresponding setting value changed for log on fly
    Given I have a config file in my project (watch mode is enabled)
    When I change "logs" setting on the fly (level, filter, etc.), (see How config works for supported ways)
    Then The corresponding setting value has been changed to the passed one

  Scenario: Default values of logs
    Given I have a config file in my project
    When I don't specify 'logs' setting in the config file
    Then Default 'level' 'info' is used
    And Default 'transports.file.name' 'refinitiv-data-platform-lib.log' is used

# sessions

  @Desktop-session
  Scenario: Default base url for Desktop session
    Given I have a config file in my project
    When I don't specify 'sessions.desktop.default-session.base-url' setting in the config file
    Then Default base url 'http://localhost:9000' is used

  Scenario: All the requests are send to the specified domain
    Given I have a config file in my project
    When I set sessions.<name>.default-session.base-url setting to 'https://domain.com'
    Then All the requests, related to this session are send to the specified 'https://domain.com'

  Scenario: Default path for handshake
    Given I have a config file in my project
    When I create a desktop session
    Then Default path for the handshake '/api/handshake' is used

  Scenario: Default platform path
    Given I have a config file in my project
    When I create a desktop session
    Then Default platform path for the RDP '/api/rdp' is used
    And Default platform path for the UDF platform '/api/udf' is used

  @Platform-session
  Scenario: Default base url for Platform session
    Given I have a config file in my project
    When I don't specify 'sessions.platform.default-session.base-url' setting in the config file
    Then Default base url 'https://api.refinitiv.com' is used

    # TODO investigate - create ticket
  Scenario: New host is used to retrieve data from the TREP
    Given I have a config file in my project
    When I set "sessions.platform.default-session.trep-host" setting in the config file to "10.67.4.28:15000"
    Then New host "10.67.4.28:15000" is used to retrieve data from the TREP
  #  Note: You still can override this setting in the config file by passing 'deployed_platform_host' parameter in your source code when create the Platform session:

  Scenario: Default auth values
    Given I have a config file in my project
    When I don't specify 'sessions.platform.default-session.auth' endpoints in the configuration file
    Then Default 'url' '/auth/oauth2/v1' is used
    And Default 'token' '/token' is used
    And Default 'authorize' '/authorize' is used

  @Common
  Scenario: Override any of default
    Given I have a config file in my project
    When Override any of default platform/desktop session configuration (auth, handshake-url, platform-paths)
    Then New (overridden) values are used for the sessions configuration

    # TODO investigate - create ticket
  Scenario: Specify 'endpoints' section
    Given I have a config file in my project
    When Specify 'endpoints' section within 'sessions' configuration
    Then This 'sessions' endpoints override common endpoints.

# historical-pricing

  Scenario: Set historical-pricing base path
    Given I have a config file in my project
    When I set "apis.data.historical-pricing.url" setting to "/test-historical-pricing"
#    When I set "endpoints.historical-pricing.url" setting to "/historical-pricing"
    Then '/test-historical-pricing' base path is used for the historical-pricing content object creation

  Scenario: Don't set historical-pricing base path
    Given I have a config file in my project
    When I don't specify 'apis.data.historical-pricing.url' setting in the config file
    Then Default base path '/data/historical-pricing/v1' for the historical-pricing content object is used

  Scenario: Set historical-pricing events path
    Given I have a config file in my project
    When I set "apis.data.historical-pricing.endpoints.events" setting to "/test-events"
    Then '/test-events' subpath to receive historical-pricing events is used

  Scenario: Don't set historical-pricing events path
    Given I have a config file in my project
    When I don't specify 'apis.data.historical-pricing.endpoints.events' setting in the config file
    Then Default subpath '/views/events' for the historical-pricing events endpoint is used

  Scenario: Set historical-pricing interday-summaries path
    Given I have a config file in my project
    When I set "apis.data.historical-pricing.endpoints.interday-summaries" setting to "/test-interday-summaries"
    Then '/test-interday-summaries' subpath to receive an appropriate historical-pricing interday summaries is used

  Scenario: Don't set historical-pricing interday-summaries path
    Given I have a config file in my project
    When I don't specify 'apis.data.historical-pricing.endpoints.interday-summaries' setting in the config file
    Then Default subpath '/views/interday-summaries' to receive an appropriate historical-pricing interday summaries is used

  Scenario: Set historical-pricing intraday-summaries path
    Given I have a config file in my project
    When I set "apis.data.historical-pricing.endpoints.intraday-summaries" setting to "/test-intraday-summaries"
    Then '/test-intraday-summaries' subpath to receive an appropriate historical-pricing intraday summaries is used

  Scenario: Don't set historical-pricing intraday-summaries path
    Given I have a config file in my project
    When I don't specify 'apis.data.historical-pricing.endpoints.intraday-summaries' setting in the config file
    Then Default subpath '/views/intraday-summaries' to receive an appropriate historical-pricing intraday summaries is used

# quantitative-analytics-financial-contracts

  Scenario: Set quantitative-analytics-financial-contracts path
    Given I have a config file in my project
    When I set "apis.data.quantitative-analytics-financial-contracts.url" setting to "/test-quantitative-analytics"
    Then '/test-quantitative-analytics' base path is used for the quantitative-analytics-financial-contracts content object creation

  Scenario: Don't set quantitative-analytics-financial-contracts path
    Given I have a config file in my project
    When I don't specify 'apis.data.quantitative-analytics-financial-contracts.url' setting in the config file
    Then Default base path '/data/quantitative-analytics/v1' for the quantitative-analytics-financial-contracts content object is used

  Scenario: Set financial-contracts path
    Given I have a config file in my project
    When I set "apis.data.quantitative-analytics-financial-contracts.endpoints.financial-contracts" setting to "/fin-con"
    Then '/fin-con' subpath to receive financial-contracts data is used

  Scenario: Don't set financial-contracts path
    Given I have a config file in my project
    When I don't specify 'apis.data.quantitative-analytics-financial-contracts.endpoints.financial-contracts' setting in the config file
    Then Default subpath '/financial-contracts' for the quantitative-analytics-financial-contracts endpoint is used

# quantitative-analytics-curves-and-surfaces

  Scenario: Set quantitative-analytics-curves-and-surfaces path
    Given I have a config file in my project
    When I set "apis.data.quantitative-analytics-curves-and-surfaces.url" setting to "/test-curves-and-surfaces"
    Then '/test-curves-and-surfaces' base path is used for the quantitative-analytics-curves-and-surfaces content object creation

  Scenario: Don't set quantitative-analytics-curves-and-surfaces path
    Given I have a config file in my project
    When I don't specify 'apis.data.quantitative-analytics-curves-and-surfaces.url' setting in the config file
    Then Default base path '/data/quantitative-analytics-curves-and-surfaces/v1' for the quantitative-analytics-curves-and-surfaces content object is used

  Scenario: Set forward-curves path
    Given I have a config file in my project
    When I set "apis.data.quantitative-analytics-curves-and-surfaces.endpoints.forward-curves" setting to "/test-forward-curves"
    Then '/test-forward-curves' subpath to receive forward-curves data is used

  Scenario: Don't set forward-curves path
    Given I have a config file in my project
    When I don't specify 'apis.data.quantitative-analytics-curves-and-surfaces.endpoints.forward-curves' setting in the config file
    Then Default subpath '/curves/forward-curves' for the forward-curves endpoint is used

  Scenario: Set surfaces path
    Given I have a config file in my project
    When I set "apis.data.quantitative-analytics-curves-and-surfaces.endpoints.surfaces" setting to "/surf"
    Then '/surf' subpath to receive surfaces data is used

  Scenario: Don't set surfaces path
    Given I have a config file in my project
    When I don't specify 'apis.data.quantitative-analytics-curves-and-surfaces.endpoints.surfaces' setting in the config file
    Then Default subpath '/surfaces' for the surfaces endpoint is used

# news

  Scenario: Set news base path
    Given I have a config file in my project
    When I set "apis.data.news.url" setting to "/test-news"
    Then '/test-news' base path is used for the news content object creation

  Scenario: Don't set news base path
    Given I have a config file in my project
    When I don't specify 'apis.data.news.url' setting in the config file
    Then Default base path '/data/news/v1' for the news content object is used

  Scenario: Set headlines path
    Given I have a config file in my project
    When I set "apis.data.news.endpoints.headlines" setting to "/hlines"
    Then '/hlines' subpath to receive headlines data is used

  Scenario: Don't set headlines path
    Given I have a config file in my project
    When I don't specify 'apis.data.news.endpoints.headlines' setting in the config file
    Then Default subpath '/headlines' for the headlines endpoint is used

  Scenario: Set stories path
    Given I have a config file in my project
    When I set "apis.data.news.endpoints.stories" setting to "/str"
    Then '/str' subpath to receive news stories data is used

  Scenario: Don't set stories path
    Given I have a config file in my project
    When I don't specify 'apis.data.news.endpoints.stories' setting in the config file
    Then Default subpath '/stories' for the news stories endpoint is used

# search

  Scenario: Set search base path
    Given I have a config file in my project
    When I set "apis.discovery.search.url" setting to "/test-search"
    Then '/test-search' base path is used for the search content object creation

  Scenario: Don't set search base path
    Given I have a config file in my project
    When I don't specify 'apis.discovery.search.url' setting in the config file
    Then Default base path '/search/beta1' for the search content object is used

  Scenario: Set search path
    Given I have a config file in my project
    When I set "apis.discovery.search.endpoints.search" setting to "/path"
    Then '/path' subpath to receive search data is used

  Scenario: Don't set search path
    Given I have a config file in my project
    When I don't specify 'endpoints.search.search' setting in the config file
    Then Default subpath '/' for the search endpoint is used

  Scenario: Set lookup path
    Given I have a config file in my project
    When I set "apis.discovery.search.endpoints.lookup" setting to "/test-lookup"
    Then '/test-lookup' subpath to receive lookup data is used

  Scenario: Don't set lookup path
    Given I have a config file in my project
    When I don't specify 'apis.discovery.search.endpoints.lookup' setting in the config file
    Then Default subpath '/lookup' for the lookup endpoint is used

  Scenario: Set metadata path
    Given I have a config file in my project
    When I set "apis.discovery.search.endpoints.metadata" setting to "/test-metadata"
    Then '/test-metadata' subpath to receive metadata data is used

  Scenario: Don't set metadata path
    Given I have a config file in my project
    When I don't specify 'apis.discovery.search.endpoints.metadata' setting in the config file
    Then Default subpath '/metadata/views' for the metadata endpoint is used

# environmental-social-governance

  Scenario: Set ESG base path
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.url" setting to "/test-environmental-social-governance"
    Then '/test-environmental-social-governance' base path is used for the environmental-social-governance content object creation

  Scenario: Don't set ESG base path
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.url' setting in the config file
    Then Default base path '/data/environmental-social-governance/v1' for the environmental-social-governance content object is used

  Scenario: Set ESG universe subpath
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.endpoints.universe" setting to "/univ-test"
    Then '/univ-test' subpath to receive 'universe' data is used

  Scenario: Don't set ESG universe subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.endpoints.universe' setting in the config file
    Then Default subpath '/universe' for the 'universe' endpoint is used

  Scenario: Set ESG basic subpath
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.endpoints.basic" setting to "/basic-test"
    Then '/basic-test' subpath to receive 'basic' data is used

  Scenario: Don't set ESG basic subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.endpoints.basic' setting in the config file
    Then Default subpath '/views/basic' for the 'basic' endpoint is used

  Scenario: Set ESG measures-full subpath
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.endpoints.measures-full" setting to "/measures-full-test"
    Then '/measures-full-test' subpath to receive 'measures-full' data is used

  Scenario: Don't set ESG measures-full subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.endpoints.measures-full' setting in the config file
    Then Default subpath '/views/measures-full' for the 'measures-full' endpoint is used

  Scenario: Set ESG measures-standard subpath
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.endpoints.measures-standard" setting to "/measures-standard-test"
    Then '/measures-standard-test' subpath to receive 'measures-standard' data is used

  Scenario: Don't set ESG measures-standard subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.endpoints.measures-standard' setting in the config file
    Then Default subpath '/views/measures-standard' for the 'measures-standard' endpoint is used

  Scenario: Set ESG scores-full subpath
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.endpoints.scores-full" setting to "/scores-full-test"
    Then '/scores-full-test' subpath to receive 'scores-full' data is used

  Scenario: Don't set ESG scores-full subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.endpoints.scores-full' setting in the config file
    Then Default subpath '/views/scores-full' for the 'scores-full' endpoint is used

  Scenario: Set ESG scores-standard subpath
    Given I have a config file in my project
    When I set "apis.data.environmental-social-governance.endpoints.scores-standard" setting to "/scores-standard-test"
    Then '/scores-standard-test' subpath to receive 'scores-standard' data is used

  Scenario: Don't set ESG scores-standard subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.environmental-social-governance.endpoints.scores-standard' setting in the config file
    Then Default subpath '/views/scores-standard' for the 'scores-standard' endpoint is used

# datagrid

  Scenario: Set datagrid base path
    Given I have a config file in my project
    When I set "apis.data.datagrid.url" setting to "/datagrid-test"
    Then '/datagrid-test' base path is used for the datagrid object creation

  Scenario: Don't set datagrid base path
    Given I have a config file in my project
    When I don't specify 'apis.data.datagrid.url' setting in the config file
    Then Default datagrid base path '/data/datagrid/beta1' is used

  Scenario: Set datagrid standard subpath
    Given I have a config file in my project
    When I set "apis.data.datagrid.endpoints.standard" setting to "/std"
    Then '/std' subpath to receive info about datagrid data is used

  Scenario: Don't set datagrid standard subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.datagrid.endpoints.standard' setting in the config file
    Then Default subpath '/' for the datagrid endpoint is used

# pricing

  Scenario: Set pricing base path
    Given I have a config file in my project
    When I set "apis.data.pricing.url" setting to "/pricing-test"
    Then '/pricing-test' base path is used for the pricing object creation

  Scenario: Don't set pricing base path
    Given I have a config file in my project
    When I don't specify 'apis.data.pricing.url' setting in the config file
    Then Default pricing base path '/data/pricing/beta3' is used

  Scenario: Set pricing snapshots subpath
    Given I have a config file in my project
    When I set "apis.data.pricing.endpoints.snapshots" setting to "/snp"
    Then '/snp' subpath to receive info about snapshots data is used

  Scenario: Don't set pricing snapshots subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.pricing.endpoints.snapshots' setting in the config file
    Then Default subpath '/snapshots' for the snapshots endpoint is used

  Scenario: Set pricing chains subpath
    Given I have a config file in my project
    When I set "apis.data.pricing.endpoints.chains" setting to "/chn"
    Then '/chn' subpath to receive info about chains data is used

  Scenario: Don't set pricing chains subpath
    Given I have a config file in my project
    When I don't specify 'apis.data.pricing.endpoints.chains' setting in the config file
    Then Default subpath '/views/chains' for the chains endpoint is used

# streaming

  Scenario: Default values for streaming connections
    Given I do not have my custom configuration file in the project
    When I create streaming connections
    Then Default values listed bellow are used.
    """
    {
      "apis": {
        "streaming": {
            "pricing": {
                "url": "/streaming/pricing/v1",
                "endpoints": {
                    "main": {
                        "path": "/",
                        "protocols": ["OMM"],
                        "locations": []
                    }
                }
            },
            "trading-analytics": {
                "url": "/streaming/trading-analytics/trade-data/beta1",
                "endpoints": {
                    "redi": {
                        "path": "/redi",
                        "protocols": ["OMM", "RDP"],
                        "locations": []
                    }
                }
            }
        }
      }
    }

    """

    # TODO investigate - the 'OMMItemStream' object has no attribute 'connection'
  Scenario: Default streaming connection name
    Given I have my custom configuration file in the project
    When I create ItemStream/StreamingPrice connection without specify an optional parameter 'connection'
    Then 'pricing' streaming connection is used by default.

    # TODO investigate (ticket)
  @skip
  @platform-session-only
  Scenario: Locations array is used to limit the list of available connections
    Given I have my custom configuration file in the project
    When I create ItemStream/StreamingPrice connection
    Then The 'locations' array from the corresponding connection config is used to limit the list of available connections
  # Available locations list, see chapter 'How to build the websocket endpoints list'

  # TODO investigate (ticket)
  @skip
  Scenario: The url from the connection config is used as streaming discovery endpoint
    Given I have my custom configuration file in the project
    When I create ItemStream/StreamingPrice connection
    Then The 'url' from the connection config is used as streaming discovery endpoint

    # TODO investigate (ticket)
  @skip
  @desktop-session-only
  Scenario: Platform path is used for the streaming-discovery endpoint
    Given I have my custom configuration file in the project
    When I create ItemStream/StreamingPrice connection
    And I use a desktop-session
    Then '/api/rdp' platform path is used for the streaming-discovery endpoint

    # TODO investigate (ticket)
  @skip
  Scenario: Set streaming connection type and receive a corresponding error
    Given I have my custom configuration file in the project
    When I set streaming connection type to not 'OMM'
    Then I receive a corresponding error
